"""Consistent Hashing with Virtual Nodes Simulation.

Features:
- Cryptographic hash ring (MD5 based).
- Configurable virtual nodes to eliminate hot spots.
- Minimal key remapping when nodes are added or removed: O(K / N).
"""

from __future__ import annotations
import hashlib
import bisect
from typing import Dict, List, Optional


class ConsistentHashRing:
    def __init__(self, replicas: int = 100) -> None:
        self.replicas = replicas
        self.ring: List[int] = []
        self.hash_to_node: Dict[int, str] = {}
        self.nodes: set[str] = set()

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)

    def add_node(self, node: str) -> None:
        self.nodes.add(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#vnode_{i}"
            h = self._hash(vnode_key)
            bisect.insort(self.ring, h)
            self.hash_to_node[h] = node

    def remove_node(self, node: str) -> None:
        if node not in self.nodes:
            return
        self.nodes.remove(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#vnode_{i}"
            h = self._hash(vnode_key)
            idx = bisect.bisect_left(self.ring, h)
            if idx < len(self.ring) and self.ring[idx] == h:
                del self.ring[idx]
            self.hash_to_node.pop(h, None)

    def get_node(self, key: str) -> Optional[str]:
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0  # Wrap around ring
        return self.hash_to_node[self.ring[idx]]


def run_tests() -> None:
    ring = ConsistentHashRing(replicas=50)
    for n in ["node_A", "node_B", "node_C"]:
        ring.add_node(n)

    # 10,000 keys distributed across nodes
    key_mapping = {f"user_session_{i}": ring.get_node(f"user_session_{i}") for i in range(1000)}
    counts = {n: sum(1 for target in key_mapping.values() if target == n) for n in ["node_A", "node_B", "node_C"]}

    # Distribution balance: Each node should hold between 20% and 45% of traffic
    for n, count in counts.items():
        assert 200 <= count <= 480, f"Unbalanced node {n}: {count}"

    # Add node_D: Only ~25% of keys should relocate
    ring.add_node("node_D")
    relocated = sum(1 for k, old_node in key_mapping.items() if ring.get_node(k) != old_node)
    # Expected remapped keys: ~ 1000 / 4 = 250
    assert 150 <= relocated <= 350, f"Too many relocated keys: {relocated}"
    print("✅ consistent_hashing tests passed!")


if __name__ == "__main__":
    run_tests()
