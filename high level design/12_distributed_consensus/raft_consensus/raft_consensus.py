"""Raft Consensus (Election & Replication State Machine) Simulation."""
class RaftNode:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.state = "FOLLOWER"

    def request_vote(self, term: int, candidate_id: int) -> bool:
        if term > self.term:
            self.term = term
            self.voted_for = candidate_id
            return True
        return False

    def append_entries(self, term: int, entries: list) -> bool:
        if term >= self.term:
            self.term = term
            self.log.extend(entries)
            self.commit_index = len(self.log)
            return True
        return False

def run_tests():
    n1 = RaftNode(1)
    assert n1.request_vote(term=1, candidate_id=2) is True
    assert n1.append_entries(term=1, entries=["CMD_SET_X_10"]) is True
    assert n1.commit_index == 1
    print("✅ raft_consensus passed!")

if __name__ == "__main__":
    run_tests()
