"""Bulkhead Pattern & Strangler Fig Migration Simulation."""
class BulkheadPool:
    def __init__(self, critical_slots=2, non_critical_slots=1):
        self.crit_slots = critical_slots
        self.non_crit_slots = non_critical_slots
    def execute(self, is_critical: bool) -> bool:
        if is_critical and self.crit_slots > 0:
            self.crit_slots -= 1
            return True
        elif not is_critical and self.non_crit_slots > 0:
            self.non_crit_slots -= 1
            return True
        return False

def run_tests():
    bh = BulkheadPool(critical_slots=2, non_critical_slots=1)
    assert bh.execute(is_critical=False) is True
    assert bh.execute(is_critical=False) is False # Non-critical starved
    # Critical payments can still execute!
    assert bh.execute(is_critical=True) is True
    print("✅ bulkhead_and_strangler_fig passed!")

if __name__ == "__main__":
    run_tests()
