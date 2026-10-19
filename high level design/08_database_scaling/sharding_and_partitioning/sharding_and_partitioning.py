"""Database Sharding (Hash-Based) Simulation."""
import hashlib

class ShardedDB:
    def __init__(self, num_shards=3):
        self.shards = {i: {} for i in range(num_shards)}
    def _shard_id(self, key: str) -> int:
        h = int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)
        return h % len(self.shards)
    def set(self, k: str, v: str):
        sid = self._shard_id(k)
        self.shards[sid][k] = v
    def get(self, k: str) -> str:
        sid = self._shard_id(k)
        return self.shards[sid].get(k)

def run_tests():
    s = ShardedDB(3)
    s.set("user_101", "Alice")
    s.set("user_102", "Bob")
    assert s.get("user_101") == "Alice"
    assert s.get("user_102") == "Bob"
    # Ensure keys were placed across shards
    assert sum(len(store) for store in s.shards.values()) == 2
    print("✅ sharding_and_partitioning passed!")

if __name__ == "__main__":
    run_tests()
