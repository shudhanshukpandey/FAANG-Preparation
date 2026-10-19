"""Rate Limiter Service: Production multi-tier rate limiter with decorator support."""

import functools
import time
from typing import Dict, List, Tuple, Callable, Any


class UserTierLimit:
    LIMITS: Dict[str, Tuple[int, float]] = {
        # Tier: (max_requests, window_seconds)
        "FREE": (3, 1.0),      # 3 requests per 1 second
        "PRO": (10, 1.0),      # 10 requests per 1 second
        "INTERNAL": (1000, 1.0)
    }


class RateLimiterService:
    def __init__(self) -> None:
        self._user_timestamps: Dict[str, List[float]] = {}

    def check_limit(self, client_id: str, tier: str = "FREE") -> Tuple[bool, dict]:
        max_requests, window_sec = UserTierLimit.LIMITS.get(tier, UserTierLimit.LIMITS["FREE"])
        now = time.time()
        window_start = now - window_sec

        if client_id not in self._user_timestamps:
            self._user_timestamps[client_id] = []

        # Filter out expired timestamps
        active_timestamps = [ts for ts in self._user_timestamps[client_id] if ts > window_start]
        self._user_timestamps[client_id] = active_timestamps

        current_count = len(active_timestamps)
        remaining = max(0, max_requests - current_count)

        headers = {
            "X-RateLimit-Limit": str(max_requests),
            "X-RateLimit-Remaining": str(remaining),
            "X-RateLimit-Window-Sec": str(window_sec),
        }

        if current_count < max_requests:
            active_timestamps.append(now)
            headers["X-RateLimit-Remaining"] = str(remaining - 1)
            return True, headers
        else:
            oldest_timestamp = active_timestamps[0]
            retry_after = round(window_sec - (now - oldest_timestamp), 2)
            headers["Retry-After"] = str(max(0.1, retry_after))
            return False, headers


# Decorator wrapper for FastAPI / Flask endpoints
def rate_limit(service: RateLimiterService, client_id_extractor: Callable[..., str], tier_extractor: Callable[..., str]):
    def decorator(func: Callable[..., Any]):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            client_id = client_id_extractor(*args, **kwargs)
            tier = tier_extractor(*args, **kwargs)

            allowed, headers = service.check_limit(client_id, tier)
            if not allowed:
                return {
                    "status_code": 429,
                    "body": {"error": "Too Many Requests", "retry_after": headers.get("Retry-After")},
                    "headers": headers
                }

            result = func(*args, **kwargs)
            result["headers"] = headers
            return result
        return wrapper
    return decorator


# Demo API Endpoint
limiter = RateLimiterService()

@rate_limit(
    service=limiter,
    client_id_extractor=lambda user, tier: user,
    tier_extractor=lambda user, tier: tier
)
def search_api(user: str, tier: str) -> dict:
    return {"status_code": 200, "body": {"results": ["item1", "item2"]}}


if __name__ == "__main__":
    print("--- Testing FREE Tier (Limit: 3 req / 1s) ---")
    for i in range(1, 5):
        resp = search_api("user_bob", tier="FREE")
        status = resp["status_code"]
        remaining = resp["headers"].get("X-RateLimit-Remaining", "0")
        print(f"Request #{i}: HTTP {status} (Remaining: {remaining})")

    print("\n--- Testing PRO Tier (Limit: 10 req / 1s) ---")
    resp_pro = search_api("user_enterprise", tier="PRO")
    print(f"PRO Request: HTTP {resp_pro['status_code']} (Remaining: {resp_pro['headers']['X-RateLimit-Remaining']})")
