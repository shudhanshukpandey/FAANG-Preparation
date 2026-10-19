"""REST vs GraphQL vs gRPC Simulation."""
def run_tests():
    # REST: Fixed resource endpoint
    rest_resp = {"id": 1, "name": "Alice", "extra": "unused"}
    # GraphQL: Exact field projection
    gql_resp = {k: v for k, v in rest_resp.items() if k in ["name"]}
    assert gql_resp == {"name": "Alice"}
    # gRPC: Binary serialized length
    binary_payload = b"\x08\x01\x12\x05Alice"
    assert len(binary_payload) < len(str(rest_resp).encode("utf-8"))
    print("✅ rest_vs_graphql_vs_grpc passed!")

if __name__ == "__main__":
    run_tests()
