"""Event Sourcing State Projection Simulation."""
class EventSourcedAccount:
    def __init__(self):
        self.events = []
    def deposit(self, amt: int):
        self.events.append(("DEPOSIT", amt))
    def withdraw(self, amt: int):
        self.events.append(("WITHDRAW", amt))
    def rebuild_balance(self) -> int:
        bal = 0
        for ev, amt in self.events:
            if ev == "DEPOSIT": bal += amt
            elif ev == "WITHDRAW": bal -= amt
        return bal

def run_tests():
    acc = EventSourcedAccount()
    acc.deposit(100)
    acc.deposit(50)
    acc.withdraw(30)
    assert acc.rebuild_balance() == 120
    print("✅ event_sourcing passed!")

if __name__ == "__main__":
    run_tests()
