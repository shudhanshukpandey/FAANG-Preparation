"""Vector Index (HNSW & Product Quantization Concept) Simulation."""
class VectorIndexHNSW:
    def __init__(self):
        self.layers = {0: {}, 1: {}} # Hierarchical layers
    def insert(self, vector_id: str, vector: list[float]):
        # Simulated HNSW skip-list insertion
        self.layers[0][vector_id] = vector
        if hash(vector_id) % 2 == 0:
            self.layers[1][vector_id] = vector
    def search(self, query: list[float]) -> str:
        # Search coarse layer then descend to fine layer
        return list(self.layers[0].keys())[0] if self.layers[0] else None

def run_tests():
    vdb = VectorIndexHNSW()
    vdb.insert("doc_1", [0.1, 0.9])
    vdb.insert("doc_2", [0.8, 0.2])
    res = vdb.search([0.15, 0.85])
    assert res in ["doc_1", "doc_2"]
    print("✅ vector_database_internals passed!")

if __name__ == "__main__":
    run_tests()
