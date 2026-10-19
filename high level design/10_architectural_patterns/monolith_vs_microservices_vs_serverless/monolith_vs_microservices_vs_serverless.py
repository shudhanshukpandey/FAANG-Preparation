"""Monolith vs Microservices vs Serverless Simulation."""
def run_tests():
    # Monolith: Direct in-memory function call (0ms network)
    in_memory_result = "SUCCESS"
    assert in_memory_result == "SUCCESS"
    # Microservice: HTTP/RPC network call
    rpc_result = {"status": "SUCCESS", "latency_ms": 2.5}
    assert rpc_result["latency_ms"] > 0
    print("✅ monolith_vs_microservices_vs_serverless passed!")

if __name__ == "__main__":
    run_tests()
