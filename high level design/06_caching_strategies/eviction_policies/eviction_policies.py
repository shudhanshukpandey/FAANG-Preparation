"""Cache Eviction Policies Simulation."""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key):
        if key not in self.cache: return None
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, val):
        if key in self.cache: self.cache.move_to_end(key)
        self.cache[key] = val
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

def run_tests():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")     # Access 'a' -> 'b' is now LRU
    c.put("c", 3)  # Evicts 'b'
    assert c.get("b") is None
    assert c.get("a") == 1
    print("✅ eviction_policies passed!")

if __name__ == "__main__":
    run_tests()
