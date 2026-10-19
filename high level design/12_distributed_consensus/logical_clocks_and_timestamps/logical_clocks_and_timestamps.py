"""Lamport Logical Clock & Vector Clock Simulation."""
class LamportClock:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.time = 0
    def tick(self) -> int:
        self.time += 1
        return self.time
    def send_event(self) -> int:
        return self.tick()
    def receive_event(self, received_time: int) -> int:
        self.time = max(self.time, received_time) + 1
        return self.time

class VectorClock:
    def __init__(self, node_id: str, cluster_nodes: list[str]):
        self.node_id = node_id
        self.clock = {n: 0 for n in cluster_nodes}
    def tick(self):
        self.clock[self.node_id] += 1
        return dict(self.clock)
    def update(self, other_clock: dict):
        for n, t in other_clock.items():
            self.clock[n] = max(self.clock.get(n, 0), t)
        self.clock[self.node_id] += 1
        return dict(self.clock)

def run_tests():
    c1, c2 = LamportClock("n1"), LamportClock("n2")
    t1 = c1.send_event() # 1
    t2 = c2.receive_event(t1) # max(0, 1) + 1 = 2
    assert t2 == 2

    vc1 = VectorClock("A", ["A", "B"])
    vc2 = VectorClock("B", ["A", "B"])
    vc1.tick() # A:1, B:0
    c_b = vc2.update(vc1.clock) # A:1, B:1
    assert c_b["A"] == 1 and c_b["B"] == 1
    print("✅ logical_clocks_and_timestamps passed!")

if __name__ == "__main__":
    run_tests()
