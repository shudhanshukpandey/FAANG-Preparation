"""Gossip Protocol & Conflict-Free Replicated Data Type (PNCounter) Simulation."""
class PNCounter:
    """Positive-Negative Counter CRDT (State-based)."""
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.p = {node_id: 0}
        self.n = {node_id: 0}
    def inc(self):
        self.p[self.node_id] += 1
    def dec(self):
        self.n[self.node_id] += 1
    def value(self) -> int:
        return sum(self.p.values()) - sum(self.n.values())
    def merge(self, other: "PNCounter"):
        for k, v in other.p.items():
            self.p[k] = max(self.p.get(k, 0), v)
        for k, v in other.n.items():
            self.n[k] = max(self.n.get(k, 0), v)

def run_tests():
    node_a = PNCounter("A")
    node_b = PNCounter("B")
    node_a.inc() # A +1
    node_b.inc() # B +1
    node_b.dec() # B -1
    node_a.merge(node_b)
    node_b.merge(node_a)
    assert node_a.value() == 1
    assert node_b.value() == 1
    print("✅ gossip_protocol_and_crdts passed!")

if __name__ == "__main__":
    run_tests()
