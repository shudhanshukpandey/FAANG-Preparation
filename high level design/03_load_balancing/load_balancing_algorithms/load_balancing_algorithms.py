"""Load Balancing Algorithms Simulation."""
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.idx = 0
    def round_robin(self):
        s = self.servers[self.idx]
        self.idx = (self.idx + 1) % len(self.servers)
        return s
    def least_connections(self, active_conns):
        return min(self.servers, key=lambda s: active_conns.get(s, 0))

def run_tests():
    lb = LoadBalancer(["s1", "s2"])
    assert lb.round_robin() == "s1"
    assert lb.round_robin() == "s2"
    assert lb.least_connections({"s1": 10, "s2": 2}) == "s2"
    print("✅ load_balancing_algorithms passed!")

if __name__ == "__main__":
    run_tests()
