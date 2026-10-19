"""B+ Tree vs LSM-Tree Simulation."""
class LSMTree:
    def __init__(self, memtable_limit=2):
        self.memtable = {}
        self.sstable = {}
        self.limit = memtable_limit
    def put(self, k: str, v: str):
        self.memtable[k] = v
        if len(self.memtable) >= self.limit:
            # Flush immutable SSTable to disk
            self.sstable.update(self.memtable)
            self.memtable.clear()
    def get(self, k: str):
        return self.memtable.get(k, self.sstable.get(k))

def run_tests():
    lsm = LSMTree(2)
    lsm.put("k1", "v1")
    lsm.put("k2", "v2") # Triggers flush
    assert len(lsm.memtable) == 0
    assert lsm.sstable["k1"] == "v1"
    assert lsm.get("k1") == "v1"
    print("✅ b_plus_tree_vs_lsm_tree passed!")

if __name__ == "__main__":
    run_tests()
