"""Primary-Replica Asynchronous Replication Simulation."""
class DatabaseReplicationCluster:
    def __init__(self):
        self.primary = {}
        self.replica = {}
        self.replication_lag = 0
    def write_primary(self, k: str, v: str):
        self.primary[k] = v
        self.replication_lag += 1
    def sync_replication(self):
        self.replica.update(self.primary)
        self.replication_lag = 0
    def read_replica(self, k: str):
        return self.replica.get(k)

def run_tests():
    c = DatabaseReplicationCluster()
    c.write_primary("balance", "100")
    # Before sync: replication lag
    assert c.read_replica("balance") is None
    c.sync_replication()
    assert c.read_replica("balance") == "100"
    print("✅ read_replication passed!")

if __name__ == "__main__":
    run_tests()
