"""Event-Driven Choreography Simulation."""
class EventBroker:
    def __init__(self):
        self.log = []
    def publish(self, event: str):
        self.log.append(event)

def run_tests():
    b = EventBroker()
    b.publish("ORDER_CREATED")
    b.publish("INVENTORY_RESERVED")
    assert b.log == ["ORDER_CREATED", "INVENTORY_RESERVED"]
    print("✅ event_driven_architecture passed!")

if __name__ == "__main__":
    run_tests()
