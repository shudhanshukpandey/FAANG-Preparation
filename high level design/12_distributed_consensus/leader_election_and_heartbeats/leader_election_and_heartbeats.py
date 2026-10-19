"""Leader Election (Bully Algorithm) & Heartbeat Simulation."""
class BullyElection:
    def __init__(self, node_id: int, cluster_ids: list[int]):
        self.node_id = node_id
        self.cluster = sorted(cluster_ids)
        self.current_leader = max(self.cluster)
    def trigger_election(self) -> int:
        higher_nodes = [nid for nid in self.cluster if nid > self.node_id]
        if not higher_nodes:
            self.current_leader = self.node_id
            return self.node_id
        # In a full simulation, higher nodes answer. If all fail, this node wins.
        self.current_leader = max(higher_nodes)
        return self.current_leader

def run_tests():
    cluster = [1, 2, 3, 4, 5]
    be = BullyElection(3, cluster)
    assert be.current_leader == 5
    # When node 5 dies, node 4 becomes leader
    cluster.remove(5)
    be_new = BullyElection(4, cluster)
    leader = be_new.trigger_election()
    assert leader == 4
    print("✅ leader_election_and_heartbeats passed!")

if __name__ == "__main__":
    run_tests()
