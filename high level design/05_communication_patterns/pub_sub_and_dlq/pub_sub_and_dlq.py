"""Pub/Sub & Dead Letter Queue (DLQ) Simulation."""
class PubSubDLQ:
    def __init__(self, max_retries=2):
        self.dlq = []
        self.max_retries = max_retries
    def process_message(self, msg: str, fail_count: int) -> str:
        if fail_count > self.max_retries:
            self.dlq.append(msg)
            return "DEAD_LETTERED"
        return "SUCCESS"

def run_tests():
    hub = PubSubDLQ(max_retries=2)
    assert hub.process_message("good_msg", fail_count=0) == "SUCCESS"
    assert hub.process_message("bad_msg", fail_count=3) == "DEAD_LETTERED"
    assert hub.dlq == ["bad_msg"]
    print("✅ pub_sub_and_dlq passed!")

if __name__ == "__main__":
    run_tests()
