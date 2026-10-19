"""Domain-Driven Design (DDD): Aggregate Roots & Domain Events.

Features:
- Aggregate Root encapsulates boundary invariants around internal entities.
- Domain Events are recorded internally when aggregate state changes.
- Event Dispatcher / Event Bus flushes domain events after aggregate commits.
- Decouples transactional domain logic from side-effects (emails, analytics).
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Type


@dataclass(frozen=True)
class DomainEvent:
    occurred_at: float = field(default_factory=time.time)


@dataclass(frozen=True)
class OrderPlacedEvent(DomainEvent):
    order_id: str = ""
    customer_id: str = ""
    total_amount: float = 0.0


@dataclass(frozen=True)
class OrderCancelledEvent(DomainEvent):
    order_id: str = ""
    reason: str = ""


class DomainEventPublisher:
    def __init__(self) -> None:
        self._handlers: Dict[Type[DomainEvent], List[Callable[[DomainEvent], None]]] = {}

    def subscribe(self, event_type: Type[DomainEvent], handler: Callable[[DomainEvent], None]) -> None:
        self._handlers.setdefault(event_type, []).append(handler)

    def publish(self, event: DomainEvent) -> None:
        for handler in self._handlers.get(type(event), []):
            handler(event)


@dataclass
class OrderLineItem:
    item_id: str
    quantity: int
    unit_price: float

    @property
    def total(self) -> float:
        return self.quantity * self.unit_price


class OrderAggregate:
    """Aggregate Root protecting invariants of an Order and its line items."""
    def __init__(self, order_id: str, customer_id: str) -> None:
        self.order_id = order_id
        self.customer_id = customer_id
        self.items: List[OrderLineItem] = []
        self.is_cancelled: bool = False
        self._domain_events: List[DomainEvent] = []

    def add_item(self, item_id: str, quantity: int, unit_price: float) -> None:
        if self.is_cancelled:
            raise ValueError("Cannot modify cancelled order")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items.append(OrderLineItem(item_id, quantity, unit_price))

    @property
    def total_amount(self) -> float:
        return sum(item.total for item in self.items)

    def place_order(self) -> None:
        if not self.items:
            raise ValueError("Cannot place an empty order")
        # Invariant checks pass -> Record domain event
        self._domain_events.append(
            OrderPlacedEvent(
                order_id=self.order_id,
                customer_id=self.customer_id,
                total_amount=self.total_amount,
            )
        )

    def cancel(self, reason: str) -> None:
        if self.is_cancelled:
            return
        self.is_cancelled = True
        self._domain_events.append(
            OrderCancelledEvent(order_id=self.order_id, reason=reason)
        )

    def pull_domain_events(self) -> List[DomainEvent]:
        events = list(self._domain_events)
        self._domain_events.clear()
        return events


def run_tests() -> None:
    bus = DomainEventPublisher()
    dispatched_events = []

    bus.subscribe(OrderPlacedEvent, lambda e: dispatched_events.append(("placed", e)))
    bus.subscribe(OrderCancelledEvent, lambda e: dispatched_events.append(("cancelled", e)))

    order = OrderAggregate("ord_101", "cust_55")
    order.add_item("item_laptop", 1, 1200.0)
    order.add_item("item_mouse", 2, 25.0)

    assert order.total_amount == 1250.0

    order.place_order()
    events = order.pull_domain_events()
    assert len(events) == 1
    assert isinstance(events[0], OrderPlacedEvent)

    # Dispatch events
    for ev in events:
        bus.publish(ev)

    assert len(dispatched_events) == 1
    assert dispatched_events[0][0] == "placed"
    assert dispatched_events[0][1].total_amount == 1250.0

    # Cancel order
    order.cancel("Customer requested")
    events = order.pull_domain_events()
    for ev in events:
        bus.publish(ev)

    assert len(dispatched_events) == 2
    assert dispatched_events[1][0] == "cancelled"

    print("✅ domain_events_and_aggregates tests passed successfully!")


if __name__ == "__main__":
    run_tests()
