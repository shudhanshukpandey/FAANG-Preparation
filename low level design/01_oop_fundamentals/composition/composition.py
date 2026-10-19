"""Composition: Strong whole-part relationship where parts cannot exist without the whole."""

from typing import List


class OrderItem:
    def __init__(self, sku: str, quantity: int, unit_price: float) -> None:
        self.sku = sku
        self.quantity = quantity
        self.unit_price = unit_price

    @property
    def total_price(self) -> float:
        return self.quantity * self.unit_price

    def __repr__(self) -> str:
        return f"OrderItem(sku={self.sku}, qty={self.quantity}, total=${self.total_price:.2f})"


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        # Composition: The Order internally creates and completely manages the lifecycle of OrderItems
        self._items: List[OrderItem] = []

    def add_item(self, sku: str, quantity: int, unit_price: float) -> None:
        # Created directly within the container
        item = OrderItem(sku, quantity, unit_price)
        self._items.append(item)

    @property
    def grand_total(self) -> float:
        return sum(item.total_price for item in self._items)

    def describe(self) -> str:
        lines = [f"Order #{self.order_id} (Total: ${self.grand_total:.2f}):"]
        for item in self._items:
            lines.append(f"  - {item}")
        return "\n".join(lines)


if __name__ == "__main__":
    order = Order("ORD-9901")
    order.add_item("LAPTOP-PRO", 1, 1499.99)
    order.add_item("WIRELESS-MOUSE", 2, 29.50)

    print(order.describe())

    # When the order is discarded, its associated item entities cannot meaningfully exist on their own
    del order
    print("Order and its internal items discarded.")
