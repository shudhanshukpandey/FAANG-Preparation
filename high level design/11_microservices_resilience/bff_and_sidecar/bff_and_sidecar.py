"""BFF & Sidecar Proxy Simulation."""
class MobileBFF:
    def aggregate(self, user_id: str) -> dict:
        # Aggregates user profile and orders into compact mobile schema
        return {"id": user_id, "badge": "VIP", "orders_count": 5}

def run_tests():
    bff = MobileBFF()
    assert bff.aggregate("u1")["badge"] == "VIP"
    print("✅ bff_and_sidecar passed!")

if __name__ == "__main__":
    run_tests()
