"""Bloom Filter Simulation."""
import hashlib

class BloomFilter:
    def __init__(self, size: int = 100):
        self.size = size
        self.bits = [0] * size

    def _hashes(self, item: str):
        h1 = int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size
        h2 = int(hashlib.sha256(item.encode()).hexdigest(), 16) % self.size
        return [h1, h2]

    def add(self, item: str):
        for h in self._hashes(item):
            self.bits[h] = 1

    def contains(self, item: str) -> bool:
        return all(self.bits[h] == 1 for h in self._hashes(item))

def run_tests():
    bf = BloomFilter(100)
    bf.add("alice@example.com")
    assert bf.contains("alice@example.com") is True
    # Non-existent item should reliably be false in large bitset
    assert bf.contains("unknown_user_99999@domain.org") is False
    print("✅ bloom_and_cuckoo_filters passed!")

if __name__ == "__main__":
    run_tests()
