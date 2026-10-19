"""Real-Time Communication (WebSocket Pub/Sub) Simulation."""
class WebSocketBroker:
    def __init__(self):
        self.subscribers = {}
    def subscribe(self, topic: str, client_id: str):
        self.subscribers.setdefault(topic, set()).add(client_id)
    def publish(self, topic: str, msg: str) -> list:
        return [f"Delivered {msg} to {c}" for c in self.subscribers.get(topic, set())]

def run_tests():
    broker = WebSocketBroker()
    broker.subscribe("chat_room_1", "user_alice")
    broker.subscribe("chat_room_1", "user_bob")
    res = broker.publish("chat_room_1", "Hello World")
    assert len(res) == 2
    print("✅ real_time_communication passed!")

if __name__ == "__main__":
    run_tests()
