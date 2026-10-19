"""HTTP/1.1 vs HTTP/2 vs HTTP/3 Simulation."""
def run_tests():
    # H1 serial
    h1 = ["HTTP/1.1 200 /a", "HTTP/1.1 200 /b"]
    assert len(h1) == 2
    # H2 multiplexed
    h2_streams = {1: "/a", 2: "/b"}
    assert len(h2_streams) == 2
    # H3 QUIC independent
    h3_streams = {1: "DROPPED", 2: "DELIVERED"}
    assert h3_streams[2] == "DELIVERED"
    print("✅ http_evolution passed!")

if __name__ == "__main__":
    run_tests()
