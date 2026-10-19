"""MapReduce Simulation."""
from collections import defaultdict

def mapper(doc_id: str, text: str) -> list[tuple[str, int]]:
    return [(word.lower(), 1) for word in text.split()]

def reducer(word: str, counts: list[int]) -> tuple[str, int]:
    return (word, sum(counts))

def run_tests():
    data = [("d1", "cat dog cat"), ("d2", "dog wolf")]
    mapped = []
    for doc_id, text in data:
        mapped.extend(mapper(doc_id, text))

    # Shuffle & Sort
    shuffled = defaultdict(list)
    for k, v in mapped:
        shuffled[k].append(v)

    reduced = dict(reducer(k, v) for k, v in shuffled.items())
    assert reduced["cat"] == 2
    assert reduced["dog"] == 2
    assert reduced["wolf"] == 1
    print("✅ mapreduce_pipeline passed!")

if __name__ == "__main__":
    run_tests()
