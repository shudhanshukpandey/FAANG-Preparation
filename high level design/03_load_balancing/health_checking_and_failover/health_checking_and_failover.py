"""Health Checking & Failover Simulation."""
class HealthChecker:
    def __init__(self, fail_threshold=2):
        self.fails = {}
        self.threshold = fail_threshold
    def record_probe(self, server, ok):
        if ok:
            self.fails[server] = 0
        else:
            self.fails[server] = self.fails.get(server, 0) + 1
    def is_healthy(self, server):
        return self.fails.get(server, 0) < self.threshold

def run_tests():
    hc = HealthChecker(fail_threshold=2)
    hc.record_probe("s1", False)
    assert hc.is_healthy("s1") is True  # 1 failure: not yet dead
    hc.record_probe("s1", False)
    assert hc.is_healthy("s1") is False # 2 failures: marked dead
    print("✅ health_checking_and_failover passed!")

if __name__ == "__main__":
    run_tests()
