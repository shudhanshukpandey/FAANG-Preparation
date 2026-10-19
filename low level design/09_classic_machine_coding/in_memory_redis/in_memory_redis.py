"""In-Memory Key-Value Store (Mini-Redis).

Features:
- String and Hash data structures (SET, GET, DEL, HSET, HGET, HGETALL).
- Active and Passive TTL expiration.
- Atomic Multi-key Transactions (MULTI, EXEC, DISCARD) with rollback support.
- Thread-safe operations using fine-grained synchronization.
"""

from __future__ import annotations

import time
import threading
from typing import Any, Dict, List, Optional, Callable


class KeyValueEntry:
    def __init__(self, value: Any, expire_at: Optional[float] = None) -> None:
        self.value = value
        self.expire_at = expire_at

    def is_expired(self) -> bool:
        if self.expire_at is None:
            return False
        return time.time() >= self.expire_at


class InMemoryRedis:
    def __init__(self) -> None:
        self._store: Dict[str, KeyValueEntry] = {}
        self._lock = threading.RLock()
        self._local_tx = threading.local()

    def _get_tx_queue(self) -> Optional[List[Callable[[], Any]]]:
        return getattr(self._local_tx, "queue", None)

    # -------------------------------------------------------------
    # String Operations
    # -------------------------------------------------------------
    def set(self, key: str, value: Any, ttl_seconds: Optional[float] = None) -> str:
        q = self._get_tx_queue()
        if q is not None:
            q.append(lambda: self.set(key, value, ttl_seconds))
            return "QUEUED"

        expire_at = time.time() + ttl_seconds if ttl_seconds is not None else None
        with self._lock:
            self._store[key] = KeyValueEntry(value, expire_at)
        return "OK"

    def get(self, key: str) -> Optional[Any]:
        q = self._get_tx_queue()
        if q is not None:
            raise RuntimeError("Cannot execute read operations inside a queued transaction")

        with self._lock:
            entry = self._store.get(key)
            if not entry:
                return None
            if entry.is_expired():
                del self._store[key]
                return None
            return entry.value

    def delete(self, key: str) -> bool:
        q = self._get_tx_queue()
        if q is not None:
            q.append(lambda: self.delete(key))
            return True  # Queued indicator

        with self._lock:
            entry = self._store.pop(key, None)
            return entry is not None and not entry.is_expired()

    # -------------------------------------------------------------
    # Hash Operations
    # -------------------------------------------------------------
    def hset(self, key: str, field: str, value: Any) -> int:
        q = self._get_tx_queue()
        if q is not None:
            q.append(lambda: self.hset(key, field, value))
            return 1

        with self._lock:
            entry = self._store.get(key)
            if entry and entry.is_expired():
                del self._store[key]
                entry = None

            if entry is None:
                hash_map: Dict[str, Any] = {}
                self._store[key] = KeyValueEntry(hash_map)
                entry = self._store[key]

            if not isinstance(entry.value, dict):
                raise TypeError(f"WRONGTYPE Operation against key '{key}' holding a non-hash value")

            is_new = field not in entry.value
            entry.value[field] = value
            return 1 if is_new else 0

    def hget(self, key: str, field: str) -> Optional[Any]:
        with self._lock:
            entry = self._store.get(key)
            if not entry or entry.is_expired():
                return None
            if not isinstance(entry.value, dict):
                raise TypeError(f"WRONGTYPE Operation against key '{key}'")
            return entry.value.get(field)

    def hgetall(self, key: str) -> Dict[str, Any]:
        with self._lock:
            entry = self._store.get(key)
            if not entry or entry.is_expired():
                return {}
            if not isinstance(entry.value, dict):
                raise TypeError(f"WRONGTYPE Operation against key '{key}'")
            return dict(entry.value)

    # -------------------------------------------------------------
    # TTL & Expire Management
    # -------------------------------------------------------------
    def expire(self, key: str, ttl_seconds: float) -> bool:
        with self._lock:
            entry = self._store.get(key)
            if not entry or entry.is_expired():
                return False
            entry.expire_at = time.time() + ttl_seconds
            return True

    def ttl(self, key: str) -> int:
        with self._lock:
            entry = self._store.get(key)
            if not entry:
                return -2  # Key does not exist
            if entry.is_expired():
                del self._store[key]
                return -2
            if entry.expire_at is None:
                return -1  # Key exists but has no expiration
            remaining = int(entry.expire_at - time.time())
            return max(0, remaining)

    # -------------------------------------------------------------
    # Atomic Transactions (MULTI / EXEC / DISCARD)
    # -------------------------------------------------------------
    def multi(self) -> str:
        if self._get_tx_queue() is not None:
            raise RuntimeError("MULTI calls cannot be nested")
        self._local_tx.queue = []
        return "OK"

    def discard(self) -> str:
        if self._get_tx_queue() is None:
            raise RuntimeError("DISCARD without MULTI")
        self._local_tx.queue = None
        return "OK"

    def exec(self) -> List[Any]:
        queue = self._get_tx_queue()
        if queue is None:
            raise RuntimeError("EXEC without MULTI")

        # Disable queue before running so operations inside commit execute directly
        self._local_tx.queue = None
        results = []
        with self._lock:
            for op in queue:
                results.append(op())
        return results


def run_tests() -> None:
    db = InMemoryRedis()

    # Test basic get/set
    assert db.set("user:1", "Alice") == "OK"
    assert db.get("user:1") == "Alice"
    assert db.delete("user:1") is True
    assert db.get("user:1") is None

    # Test Hash operations
    assert db.hset("session:abc", "ip", "192.168.1.1") == 1
    assert db.hset("session:abc", "auth", "true") == 1
    assert db.hget("session:abc", "ip") == "192.168.1.1"
    assert db.hgetall("session:abc") == {"ip": "192.168.1.1", "auth": "true"}

    # Test TTL expiration
    db.set("temp_key", "expiring_val", ttl_seconds=0.05)
    assert db.get("temp_key") == "expiring_val"
    time.sleep(0.06)
    assert db.get("temp_key") is None
    assert db.ttl("temp_key") == -2

    # Test Multi/Exec Transaction
    db.multi()
    assert db.set("tx:a", 100) == "QUEUED"
    assert db.set("tx:b", 200) == "QUEUED"
    assert db.hset("tx:h", "k", "v") == 1
    res = db.exec()
    assert res == ["OK", "OK", 1]
    assert db.get("tx:a") == 100
    assert db.get("tx:b") == 200
    assert db.hget("tx:h", "k") == "v"

    # Test Discard
    db.multi()
    db.set("discard_key", "value")
    assert db.discard() == "OK"
    assert db.get("discard_key") is None

    print("✅ in_memory_redis tests passed successfully!")


if __name__ == "__main__":
    run_tests()
