"""Message Queue with Consumer Acknowledgements Simulation."""
class MessageQueue:
    def __init__(self):
        self.queue = []
    def produce(self, msg: str):
        self.queue.append(msg)
    def consume(self) -> str:
        return self.queue.pop(0) if self.queue else None

def run_tests():
    mq = MessageQueue()
    mq.produce("task_1")
    mq.produce("task_2")
    assert mq.consume() == "task_1"
    assert mq.consume() == "task_2"
    assert mq.consume() is None
    print("✅ message_queues passed!")

if __name__ == "__main__":
    run_tests()
