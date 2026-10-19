"""Retrieval-Augmented Generation (RAG) Pipeline Simulation."""
class RAGPipeline:
    def __init__(self):
        self.doc_index = {
            "chunk_1": ("System design involves scalability, availability and reliability.", [0.8, 0.2]),
            "chunk_2": ("Chocolate cake recipe requires flour, sugar and cocoa.", [0.1, 0.9])
        }

    def retrieve(self, query_vector: list[float], top_k=1) -> str:
        # Score similarity
        best_doc = max(self.doc_index.values(), key=lambda d: sum(a * b for a, b in zip(query_vector, d[1])))
        return best_doc[0]

    def generate(self, user_prompt: str, context: str) -> str:
        return f"LLM_ANSWER: Based on '{context}', {user_prompt} is answered."

def run_tests():
    rag = RAGPipeline()
    context = rag.retrieve([0.9, 0.1])
    ans = rag.generate("What is system design?", context)
    assert "scalability" in ans
    print("✅ rag_pipeline passed!")

if __name__ == "__main__":
    run_tests()
