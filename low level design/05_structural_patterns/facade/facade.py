"""Facade Pattern: Providing a unified, simple interface to a complex subsystem."""


# Subsystem Component 1
class InventoryService:
    def check_and_reserve(self, sku: str, quantity: int) -> bool:
        print(f"[Inventory] Reserved {quantity} units of SKU '{sku}'.")
        return True


# Subsystem Component 2
class PaymentGatewayService:
    def process_charge(self, user_id: str, amount: float) -> str:
        print(f"[Payment] Processed payment of ${amount:.2f} for user '{user_id}'.")
        return "TXN_774092"


# Subsystem Component 3
class LogisticsService:
    def generate_shipping_label(self, user_id: str, sku: str) -> str:
        print(f"[Logistics] Generated courier tracking label for SKU '{sku}'.")
        return "TRACK-FDX-9901"


# Subsystem Component 4
class NotificationService:
    def send_order_confirmation(self, user_id: str, tracking_number: str) -> None:
        print(f"[Notification] Dispatched confirmation email + SMS with tracking: {tracking_number}")


# The Facade: Encapsulates all subsystem interactions behind one clean call
class OrderFulfillmentFacade:
    def __init__(self) -> None:
        self.inventory = InventoryService()
        self.payment = PaymentGatewayService()
        self.logistics = LogisticsService()
        self.notifier = NotificationService()

    def place_order(self, user_id: str, sku: str, quantity: int, total_amount: float) -> dict:
        print(f"=== Starting Order Placement for {user_id} ===")
        # 1. Check stock
        if not self.inventory.check_and_reserve(sku, quantity):
            raise RuntimeError("Insufficient stock")

        # 2. Charge card
        txn_id = self.payment.process_charge(user_id, total_amount)

        # 3. Schedule delivery
        tracking_code = self.logistics.generate_shipping_label(user_id, sku)

        # 4. Notify customer
        self.notifier.send_order_confirmation(user_id, tracking_code)

        print("=== Order Completed Successfully ===\n")
        return {
            "status": "CONFIRMED",
            "transaction_id": txn_id,
            "tracking_code": tracking_code
        }


if __name__ == "__main__":
    # Client interaction is 1 single line!
    facade = OrderFulfillmentFacade()
    receipt = facade.place_order(user_id="user_john", sku="IPHONE-15-PRO", quantity=1, total_amount=1099.99)
    print("Client received receipt:", receipt)
