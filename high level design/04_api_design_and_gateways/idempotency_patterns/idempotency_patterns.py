"""Idempotency Key Deduplication Simulation."""
class IdempotencyEngine:
    def __init__(self):
        self.store = {}
    def execute_payment(self, key: str, amount: float) -> dict:
        if key in self.store:
            return self.store[key] # Return cached original response
        # Process payment
        res = {"status": "SUCCESS", "amount": amount, "tx_id": f"tx_{key}"}
        self.store[key] = res
        return res

def run_tests():
    engine = IdempotencyEngine()
    r1 = engine.execute_payment("idem_982", 150.0)
    assert r1["status"] == "SUCCESS"
    # Network retry with same idempotency key
    r2 = engine.execute_payment("idem_982", 150.0)
    assert r2 == r1  # Exact cached response, zero duplicate charge
    print("✅ idempotency_patterns passed!")

if __name__ == "__main__":
    run_tests()
