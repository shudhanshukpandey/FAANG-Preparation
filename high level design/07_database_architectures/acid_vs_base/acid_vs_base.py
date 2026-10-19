"""ACID vs BASE Consistency Simulation."""
class ACIDTransaction:
    def __init__(self):
        self.accounts = {"A": 500, "B": 200}
    def transfer(self, src: str, dst: str, amt: int) -> bool:
        if self.accounts[src] < amt: return False
        # Atomic commit
        self.accounts[src] -= amt
        self.accounts[dst] += amt
        return True

def run_tests():
    tx = ACIDTransaction()
    assert tx.transfer("A", "B", 100) is True
    assert tx.accounts == {"A": 400, "B": 300}
    assert tx.transfer("A", "B", 1000) is False
    assert tx.accounts == {"A": 400, "B": 300}
    print("✅ acid_vs_base passed!")

if __name__ == "__main__":
    run_tests()
