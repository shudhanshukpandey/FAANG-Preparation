"""CAP and PACELC Theorem Simulation.

Demonstrates:
- CAP Theorem trade-off during a network partition: Consistency (CP) vs Availability (AP).
- PACELC Theorem: If Partition (P) -> Availability (A) or Consistency (C); Else (E) -> Latency (L) or Consistency (C).
"""

from __future__ import annotations


class DistributedStorageNode:
    def __init__(self, node_id: str, mode: str = "CP") -> None:
        self.node_id = node_id
        self.mode = mode  # "CP" or "AP"
        self.data: dict[str, str] = {}
        self.is_partitioned = False

    def write(self, key: str, value: str) -> bool:
        if self.is_partitioned:
            if self.mode == "CP":
                # CP refuses writes to prevent split-brain inconsistencies
                raise ConnectionError("Partition detected: Write rejected to preserve Consistency")
            elif self.mode == "AP":
                # AP accepts write locally, risking divergence
                self.data[key] = value
                return True
        self.data[key] = value
        return True

    def read(self, key: str) -> str | None:
        if self.is_partitioned and self.mode == "CP":
            raise ConnectionError("Partition detected: Read rejected to prevent stale data")
        return self.data.get(key)


def run_tests() -> None:
    # CP Node (e.g. Zookeeper, Etcd, MongoDB primary)
    cp_node = DistributedStorageNode("node_1", mode="CP")
    cp_node.write("balance", "100")
    assert cp_node.read("balance") == "100"

    # Simulate network cut
    cp_node.is_partitioned = True
    try:
        cp_node.write("balance", "200")
        assert False, "Should have raised ConnectionError"
    except ConnectionError:
        pass  # Expected CP behavior

    # AP Node (e.g. Cassandra, DynamoDB, CouchDB)
    ap_node = DistributedStorageNode("node_2", mode="AP")
    ap_node.is_partitioned = True
    assert ap_node.write("cart", "laptop") is True
    assert ap_node.read("cart") == "laptop"
    print("✅ cap_and_pacelc tests passed!")


if __name__ == "__main__":
    run_tests()
