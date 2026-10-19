"""Batch vs Stream Processing Simulation."""
class StreamProcessor:
    def process_event(self, event: int) -> int:
        return event * 2 # Millisecond latency

class BatchProcessor:
    def process_batch(self, events: list[int]) -> int:
        return sum(events) * 2 # High throughput bulk processing

def run_tests():
    sp = StreamProcessor()
    bp = BatchProcessor()
    assert sp.process_event(5) == 10
    assert bp.process_batch([1, 2, 3, 4, 5]) == 30
    print("✅ batch_vs_stream_processing passed!")

if __name__ == "__main__":
    run_tests()
