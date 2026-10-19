"""Service Discovery (Consul / Eureka Style) Simulation."""
class ServiceRegistry:
    def __init__(self):
        self.registry = {}
    def register(self, svc_name: str, instance_ip: str):
        self.registry.setdefault(svc_name, []).append(instance_ip)
    def discover(self, svc_name: str) -> list:
        return self.registry.get(svc_name, [])

def run_tests():
    reg = ServiceRegistry()
    reg.register("order_svc", "10.0.0.1:8080")
    reg.register("order_svc", "10.0.0.2:8080")
    assert len(reg.discover("order_svc")) == 2
    print("✅ service_discovery passed!")

if __name__ == "__main__":
    run_tests()
