"""Cache Stampede Prevention & XFetch Probabilistic Refresh."""
import math, random, time

class XFetchCache:
    def __init__(self):
        self.cache = {}
    def set(self, key, val, ttl_sec):
        self.cache[key] = {"val": val, "expire_at": time.time() + ttl_sec, "compute_time": 0.05}
    def should_refresh(self, key: str, beta: float = 1.0) -> bool:
        entry = self.cache.get(key)
        if not entry: return True
        time_left = entry["expire_at"] - time.time()
        # XFetch formula: -delta * beta * ln(rand()) >= time_left
        rand_val = max(0.0001, random.random())
        return -(entry["compute_time"] * beta * math.log(rand_val)) >= time_left

def run_tests():
    c = XFetchCache()
    c.set("leaderboard", "data", ttl_sec=100)
    # Plenty of time left -> refresh probability is virtually 0
    assert c.should_refresh("leaderboard") is False
    c.set("dying_key", "data", ttl_sec=-1)
    # Expired -> definitely refreshed
    assert c.should_refresh("dying_key") is True
    print("✅ cache_stampede_and_warming passed!")

if __name__ == "__main__":
    run_tests()
