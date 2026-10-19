"""Erasure Coding (Parity Simulation)."""
class SimpleErasureCoder:
    """Simulates 2 data blocks + 1 XOR parity block (2+1 scheme)."""
    def encode(self, b1: int, b2: int) -> tuple[int, int, int]:
        parity = b1 ^ b2
        return (b1, b2, parity)
    def reconstruct_from_parity(self, available_block: int, parity: int) -> int:
        return available_block ^ parity

def run_tests():
    ec = SimpleErasureCoder()
    d1, d2, p = ec.encode(42, 99)
    # Block 1 lost -> reconstruct using d2 and parity
    recovered_d1 = ec.reconstruct_from_parity(d2, p)
    assert recovered_d1 == 42
    print("✅ erasure_coding passed!")

if __name__ == "__main__":
    run_tests()
