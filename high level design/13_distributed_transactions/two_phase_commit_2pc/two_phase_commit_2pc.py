"""Two-Phase Commit (2PC) Simulation."""
class TwoPhaseCommitCoordinator:
    def __init__(self, participants: list[str]):
        self.participants = participants
    def execute_transaction(self, participant_votes: dict[str, bool]) -> bool:
        # Phase 1: Prepare
        for p in self.participants:
            if not participant_votes.get(p, False):
                return False # Abort phase 2
        # Phase 2: Commit
        return True

def run_tests():
    c = TwoPhaseCommitCoordinator(["db1", "db2"])
    assert c.execute_transaction({"db1": True, "db2": True}) is True
    assert c.execute_transaction({"db1": True, "db2": False}) is False
    print("✅ two_phase_commit_2pc passed!")

if __name__ == "__main__":
    run_tests()
