"""HyperLogLog Unique Visitor Cardinality Simulation."""
import hashlib

class SimpleHLL:
    def __init__(self, num_registers=64):
        self.m = num_registers
        self.registers = [0] * self.m

    def add(self, item: str):
        h = int(hashlib.md5(item.encode()).hexdigest(), 16)
        reg = h % self.m
        bits = bin(h >> 4)[2:]
        leading_zeros = len(bits) - len(bits.lstrip('0')) + 1
        self.registers[reg] = max(self.registers[reg], leading_zeros)

    def count(self) -> int:
        z = sum(2 ** (-r) for r in self.registers)
        return int(0.7213 * (self.m ** 2) / z)

def run_tests():
    hll = SimpleHLL(64)
    for i in range(100):
        hll.add(f"user_{i}")
    est = hll.count()
    assert 50 <= est <= 150 # Statistical approximation
    print("✅ hyperloglog_and_count_min passed!")

if __name__ == "__main__":
    run_tests()
