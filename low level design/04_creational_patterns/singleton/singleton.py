"""Singleton Pattern: Thread-safe implementation with double-checked locking and Metaclass approach."""

import threading
from typing import Dict, Any, Optional


# -------------------------------------------------------------
# Approach 1: Thread-Safe Singleton via Double-Checked Locking
# -------------------------------------------------------------
class DatabaseConnectionPool:
    _instance: Optional["DatabaseConnectionPool"] = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls, *args, **kwargs) -> "DatabaseConnectionPool":
        # First check (unlocked) for high-throughput performance
        if cls._instance is None:
            with cls._lock:
                # Second check (locked) to prevent race conditions
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, max_connections: int = 10) -> None:
        if getattr(self, "_initialized", False):
            return
        self.max_connections = max_connections
        self.active_connections = 0
        self._pool_data: Dict[str, Any] = {}
        self._initialized = True
        print(f"[DatabaseConnectionPool] Initialized with capacity {max_connections}.")

    def acquire_connection(self, client_id: str) -> str:
        with self._lock:
            if self.active_connections >= self.max_connections:
                raise RuntimeError("Connection pool exhausted!")
            self.active_connections += 1
            conn_token = f"CONN-{client_id}-{self.active_connections}"
            self._pool_data[conn_token] = "ACTIVE"
            return conn_token

    def release_connection(self, conn_token: str) -> None:
        with self._lock:
            if conn_token in self._pool_data:
                del self._pool_data[conn_token]
                self.active_connections -= 1


# -------------------------------------------------------------
# Approach 2: Reusable Singleton Metaclass (Cleanest in Python)
# -------------------------------------------------------------
class SingletonMeta(type):
    """A thread-safe implementation of Singleton using a Metaclass."""
    _instances: Dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.environment: str = "PRODUCTION"
        self.debug: bool = False


if __name__ == "__main__":
    # Test 1: Verify identical instance across separate instantiations
    pool1 = DatabaseConnectionPool(max_connections=5)
    pool2 = DatabaseConnectionPool(max_connections=20)  # Re-init ignored

    print(f"pool1 is pool2? {pool1 is pool2}")  # True
    conn = pool1.acquire_connection("Worker-1")
    print(f"Acquired: {conn}, pool2 active connections: {pool2.active_connections}")

    # Test 2: Metaclass Singleton
    cfg1 = AppConfig()
    cfg2 = AppConfig()
    print(f"cfg1 is cfg2? {cfg1 is cfg2}")  # True
