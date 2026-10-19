"""Forward vs Reverse Proxy Simulation."""
class ForwardProxy:
    def request(self, target: str) -> str:
        return f"Forwarded to {target} via Proxy"

class ReverseProxy:
    def route(self, path: str) -> str:
        return f"Reverse proxy routed {path} to upstream"

def run_tests():
    fwd = ForwardProxy()
    rev = ReverseProxy()
    assert "Forwarded" in fwd.request("example.com")
    assert "upstream" in rev.route("/api/users")
    print("✅ forward_vs_reverse_proxy passed!")

if __name__ == "__main__":
    run_tests()
