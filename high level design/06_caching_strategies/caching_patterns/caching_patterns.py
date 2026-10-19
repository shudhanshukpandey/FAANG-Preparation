"""Caching Patterns Simulation: Cache-Aside vs Write-Through vs Write-Behind."""
class CacheAsideDB:
    def __init__(self):
        self.cache = {}
        self.db = {"u1": "Alice"}
    def read(self, key: str) -> str:
        if key in self.cache:
            return self.cache[key] # Cache hit
        # Cache miss
        val = self.db.get(key)
        if val:
            self.cache[key] = val
        return val

def run_tests():
    store = CacheAsideDB()
    assert "u1" not in store.cache
    assert store.read("u1") == "Alice" # Miss -> hydrates cache
    assert store.cache["u1"] == "Alice"
    assert store.read("u1") == "Alice" # Instant hit
    print("✅ caching_patterns passed!")

if __name__ == "__main__":
    run_tests()
