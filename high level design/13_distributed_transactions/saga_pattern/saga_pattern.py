"""Saga Pattern (Compensating Transactions) Simulation."""
class OrderSagaOrchestrator:
    def __init__(self):
        self.state = "INIT"
        self.actions_completed = []

    def run_saga(self, payment_success: bool, inventory_success: bool) -> bool:
        # Step 1: Charge
        if payment_success:
            self.actions_completed.append("PAYMENT_CHARGED")
        else:
            self.state = "FAILED"
            return False

        # Step 2: Inventory
        if inventory_success:
            self.actions_completed.append("INVENTORY_RESERVED")
            self.state = "SUCCESS"
            return True
        else:
            # Compensating action
            self.actions_completed.append("PAYMENT_REFUNDED")
            self.state = "COMPENSATED"
            return False

def run_tests():
    saga = OrderSagaOrchestrator()
    assert saga.run_saga(payment_success=True, inventory_success=True) is True
    assert saga.state == "SUCCESS"

    failed_saga = OrderSagaOrchestrator()
    assert failed_saga.run_saga(payment_success=True, inventory_success=False) is False
    assert failed_saga.state == "COMPENSATED"
    assert "PAYMENT_REFUNDED" in failed_saga.actions_completed
    print("✅ saga_pattern passed!")

if __name__ == "__main__":
    run_tests()
