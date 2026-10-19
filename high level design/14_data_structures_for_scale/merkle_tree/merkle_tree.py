"""Merkle Tree (Anti-Entropy Repair) Simulation."""
import hashlib

def sha(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()[:10]

class MerkleTree:
    def __init__(self, leaves: list[str]):
        self.leaves = [sha(l) for l in leaves]
        self.root = self._build(self.leaves)
    def _build(self, nodes: list[str]) -> str:
        if len(nodes) == 1:
            return nodes[0]
        parent_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            parent_level.append(sha(left + right))
        return self._build(parent_level)

def run_tests():
    t1 = MerkleTree(["chunk1", "chunk2", "chunk3", "chunk4"])
    t2 = MerkleTree(["chunk1", "chunk2", "chunk3", "chunk4"])
    assert t1.root == t2.root
    # Alter single chunk
    t3 = MerkleTree(["chunk1", "chunk2_CORRUPT", "chunk3", "chunk4"])
    assert t1.root != t3.root
    print("✅ merkle_tree passed!")

if __name__ == "__main__":
    run_tests()
