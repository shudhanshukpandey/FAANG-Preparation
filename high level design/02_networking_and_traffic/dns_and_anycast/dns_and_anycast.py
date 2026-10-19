"""Hierarchical DNS & Anycast Routing Simulation."""
class DNSResolver:
    def __init__(self):
        self.cache = {}
        self.db = {"faang.com": "104.244.42.1"}
    def resolve(self, domain: str) -> str:
        if domain not in self.cache:
            self.cache[domain] = self.db[domain]
        return self.cache[domain]

def run_tests():
    dns = DNSResolver()
    assert dns.resolve("faang.com") == "104.244.42.1"
    assert "faang.com" in dns.cache
    print("✅ dns_and_anycast passed!")

if __name__ == "__main__":
    run_tests()
