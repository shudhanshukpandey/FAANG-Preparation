"""Specialized Databases: Vector Similarity & Time-Series Simulation."""
import math

class VectorStore:
    def cosine_similarity(self, v1: list[float], v2: list[float]) -> float:
        dot = sum(a * b for a, b in zip(v1, v2))
        m1 = math.sqrt(sum(a * a for a in v1))
        m2 = math.sqrt(sum(b * b for b in v2))
        return round(dot / (m1 * m2), 4)

def run_tests():
    vs = VectorStore()
    v_apple = [0.9, 0.1, 0.0]
    v_fruit = [0.85, 0.15, 0.0]
    v_car = [0.05, 0.8, 0.9]
    sim_fruit = vs.cosine_similarity(v_apple, v_fruit)
    sim_car = vs.cosine_similarity(v_apple, v_car)
    assert sim_fruit > 0.95
    assert sim_car < 0.3
    print("✅ specialized_databases passed!")

if __name__ == "__main__":
    run_tests()
