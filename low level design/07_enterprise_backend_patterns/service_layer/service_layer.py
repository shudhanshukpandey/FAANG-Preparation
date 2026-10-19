"""Service Layer Pattern: Orchestrating domain entities, repositories, and notifications."""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Order:
    id: str
    user_id: str
    item_sku: str
    quantity: int
    total_amount: float
    status: str = "PENDING"


# Repositories
class OrderRepository:
    def __init__(self) -> None:
        self._orders: Dict[str, Order] = {}

    def save(self, order: Order) -> None:
        self._orders[order.id] = order
        print(f"[OrderRepo] Saved Order #{order.id} with status '{order.status}'.")


class InventoryRepository:
    def __init__(self) -> None:
        self._stock: Dict[str, int] = {"MACBOOK-M3": 5, "AIRPODS-PRO": 10}

    def get_stock(self, sku: str) -> int:
        return self._stock.get(sku, 0)

    def deduct_stock(self, sku: str, quantity: int) -> None:
        self._stock[sku] -= quantity
        print(f"[InventoryRepo] Deducted {quantity} of {sku}. Remaining: {self._stock[sku]}")


class EmailNotificationService:
    def send_order_receipt(self, user_id: str, order_id: str, total: float) -> None:
        print(f"[EmailNotifier] Sent receipt to user {user_id} for Order #{order_id} (${total:.2f}).")


# The Service Layer: Contains use case workflows
class OrderFulfillmentService:
    def __init__(
        self,
        order_repo: OrderRepository,
        inventory_repo: InventoryRepository,
        notifier: EmailNotificationService
    ) -> None:
        self.order_repo = order_repo
        self.inventory_repo = inventory_repo
        self.notifier = notifier

    def place_order(self, order_id: str, user_id: str, sku: str, qty: int, unit_price: float) -> Order:
        # Step 1: Validate business rule
        available_stock = self.inventory_repo.get_stock(sku)
        if available_stock < qty:
            raise ValueError(f"Out of stock! Requested {qty}, but only {available_stock} available.")

        # Step 2: Deduct inventory
        self.inventory_repo.deduct_stock(sku, qty)

        # Step 3: Create & persist domain entity
        total = qty * unit_price
        order = Order(id=order_id, user_id=user_id, item_sku=sku, quantity=qty, total_amount=total, status="CONFIRMED")
        self.order_repo.save(order)

        # Step 4: Dispatch external notification
        self.notifier.send_order_receipt(user_id, order_id, total)

        return order


# Skinny Controller (FastAPI / Flask representation)
class MockAPIController:
    def __init__(self, service: OrderFulfillmentService) -> None:
        self.service = service

    def handle_post_checkout(self, request_payload: dict) -> dict:
        # Controller only handles HTTP input/output mapping and error status
        try:
            order = self.service.place_order(
                order_id=request_payload["order_id"],
                user_id=request_payload["user_id"],
                sku=request_payload["sku"],
                qty=request_payload["quantity"],
                unit_price=request_payload["unit_price"]
            )
            return {"http_status": 201, "order_id": order.id, "status": order.status}
        except ValueError as err:
            return {"http_status": 400, "error": str(err)}


if __name__ == "__main__":
    svc = OrderFulfillmentService(OrderRepository(), InventoryRepository(), EmailNotificationService())
    controller = MockAPIController(svc)

    print("--- 1. Successful Checkout API Call ---")
    resp1 = controller.handle_post_checkout({
        "order_id": "ORD-501", "user_id": "usr_neo", "sku": "MACBOOK-M3", "quantity": 2, "unit_price": 1999.0
    })
    print("API Response:", resp1)

    print("\n--- 2. Failed Checkout (Insufficient Stock) ---")
    resp2 = controller.handle_post_checkout({
        "order_id": "ORD-502", "user_id": "usr_neo", "sku": "MACBOOK-M3", "quantity": 10, "unit_price": 1999.0
    })
    print("API Response:", resp2)
