"""Rate Limiter Pattern: Token Bucket and Sliding Window Log algorithms."""

import time
import threading
from typing import Dict, List


# -------------------------------------------------------------
# 1. Thread-Safe Token Bucket Rate Limiter
# -------------------------------------------------------------
class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate_per_sec: float) -> None:
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self.tokens: float = float(capacity)
        self.last_refill_timestamp = time.time()
        self._lock = threading.Lock()

    def _refill(self) -> None:
        now = time.time()
        elapsed = now - self.last_refill_timestamp
        added_tokens = elapsed * self.refill_rate
        self.tokens = min(float(self.capacity), self.tokens + added_tokens)
        self.last_refill_timestamp = now

    def allow_request(self, tokens_needed: int = 1) -> bool:
        with self._lock:
            self._refill()
            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            return False


# -------------------------------------------------------------
# 2. Sliding Window Log Rate Limiter (Redis ZSET in-memory simulation)
# -------------------------------------------------------------
class SlidingWindowLogRateLimiter:
    def __init__(self, max_requests: int, window_seconds: float) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._user_logs: Dict[str, List[float]] = {}
        self._lock = threading.Lock()

    def allow_request(self, user_id: str) -> bool:
        with self._lock:
            now = time.time()
            window_start = now - self.window_seconds

            if user_id not in self._user_logs:
                self._user_logs[user_id] = []

            # Evict timestamps older than the sliding window boundary
            self._user_logs[user_id] = [ts for ts in self._user_logs[user_id] if ts > window_start]

            if len(self._user_logs[user_id]) < self.max_requests:
                self._user_logs[user_id].append(now)
                return True
            return False


if __name__ == "__main__":
    print("--- 1. Testing Token Bucket (Capacity 3, Refill 1 token/sec) ---")
    tb = TokenBucketRateLimiter(capacity=3, refill_rate_per_sec=1.0)

    for i in range(1, 6):
        allowed = tb.allow_request(1)
        print(f"Request #{i}: {'Allowed ✅' if allowed else 'Rate Limited ❌ (429)'}")

    print("\nSleeping 1.1s to allow token refill...")
    time.sleep(1.1)
    print(f"Request after refill: {'Allowed ✅' if tb.allow_request(1) else 'Rate Limited ❌'}")

    print("\n--- 2. Testing Sliding Window Log (Max 2 requests per 0.5s window) ---")
    sw = SlidingWindowLogRateLimiter(max_requests=2, window_seconds=0.5)
    print("User 'Alice' req 1:", sw.allow_request("Alice"))  # True
    print("User 'Alice' req 2:", sw.allow_request("Alice"))  # True
    print("User 'Alice' req 3:", sw.allow_request("Alice"))  # False (Limit reached)
    print("User 'Bob'   req 1:", sw.allow_request("Bob"))    # True (Independent user bucket)
