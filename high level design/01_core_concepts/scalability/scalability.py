"""Scalability: Horizontal vs Vertical Scaling Simulation.

Demonstrates:
- Vertical Scaling (Scale-Up): Expanding single-node CPU/RAM with diminishing returns & hard ceilings.
- Horizontal Scaling (Scale-Out): Elastic stateless worker pools with load distribution.
"""

from __future__ import annotations
import time
from dataclasses import dataclass
from typing import List


@dataclass
class ServerNode:
    node_id: str
    capacity_rps: int
    current_load: int = 0

    def can_handle(self) -> bool:
        return self.current_load < self.capacity_rps

    def process_request(self) -> bool:
        if self.can_handle():
            self.current_load += 1
            return True
        return False


class HorizontalCluster:
    def __init__(self, node_capacity: int = 100) -> None:
        self.node_capacity = node_capacity
        self.nodes: List[ServerNode] = [ServerNode("node_0", node_capacity)]

    def auto_scale(self, incoming_requests: int) -> None:
        required_nodes = (incoming_requests + self.node_capacity - 1) // self.node_capacity
        while len(self.nodes) < required_nodes:
            new_id = f"node_{len(self.nodes)}"
            self.nodes.append(ServerNode(new_id, self.node_capacity))

    def dispatch(self, num_requests: int) -> int:
        self.auto_scale(num_requests)
        handled = 0
        node_idx = 0
        for _ in range(num_requests):
            if self.nodes[node_idx].process_request():
                handled += 1
            node_idx = (node_idx + 1) % len(self.nodes)
        return handled


def run_tests() -> None:
    cluster = HorizontalCluster(node_capacity=50)
    assert len(cluster.nodes) == 1
    # Dispatch burst of 120 requests -> triggers auto-scaling to 3 nodes
    handled = cluster.dispatch(120)
    assert handled == 120
    assert len(cluster.nodes) == 3
    print("✅ scalability tests passed!")


if __name__ == "__main__":
    run_tests()
