"""Transactional Outbox Pattern: Solving the dual-write problem for reliable messaging."""

import json
import uuid
from typing import Dict, List, Any


# 1. Database Simulation with Outbox Table
class MockDatabase:
    def __init__(self) -> None:
        self.orders: Dict[str, dict] = {}
        self.outbox_events: List[dict] = []
        self._in_transaction = False
        self._staged_orders: Dict[str, dict] = {}
        self._staged_events: List[dict] = []

    def begin(self) -> None:
        self._in_transaction = True
        self._staged_orders = {}
        self._staged_events = []

    def insert_order(self, order_id: str, data: dict) -> None:
        self._staged_orders[order_id] = data

    def insert_outbox_event(self, event_type: str, payload: dict) -> None:
        event = {
            "id": str(uuid.uuid4())[:8],
            "event_type": event_type,
            "payload": payload,
            "status": "PENDING"
        }
        self._staged_events.append(event)

    def commit(self) -> None:
        # Commit both order and event atomically
        self.orders.update(self._staged_orders)
        self.outbox_events.extend(self._staged_events)
        self._in_transaction = False
        print(f"[DB Engine] Atomically committed {len(self._staged_orders)} orders and {len(self._staged_events)} outbox events.")

    def rollback(self) -> None:
        self._staged_orders.clear()
        self._staged_events.clear()
        self._in_transaction = False
        print("[DB Engine] Rolled back transaction. Zero partial writes.")


# 2. Simulated Message Broker (e.g. Apache Kafka or RabbitMQ)
class MessageBroker:
    def publish(self, topic: str, message: dict) -> bool:
        print(f"  [Kafka Broker 🚀] Published to topic '{topic}': {message}")
        return True


# 3. Application Service
class OrderApplicationService:
    def __init__(self, db: MockDatabase) -> None:
        self.db = db

    def place_order(self, order_id: str, amount: float, customer_id: str) -> None:
        self.db.begin()
        try:
            # 1. Save Domain state
            order_data = {"id": order_id, "amount": amount, "customer_id": customer_id, "status": "CONFIRMED"}
            self.db.insert_order(order_id, order_data)

            # 2. Save Outbox event IN THE SAME LOCAL DB TRANSACTION
            event_payload = {"order_id": order_id, "amount": amount, "customer_id": customer_id}
            self.db.insert_outbox_event("OrderCreated", event_payload)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e


# 4. Outbox Relay Background Worker (e.g. Polling process or Debezium CDC)
class OutboxRelayWorker:
    def __init__(self, db: MockDatabase, broker: MessageBroker) -> None:
        self.db = db
        self.broker = broker

    def process_pending_outbox_events(self) -> None:
        print("\n[Relay Worker] Polling DB for pending outbox events...")
        for event in self.db.outbox_events:
            if event["status"] == "PENDING":
                # Publish to message broker
                success = self.broker.publish(f"events.{event['event_type'].lower()}", event["payload"])
                if success:
                    event["status"] = "PUBLISHED"
                    print(f"  [Relay Worker] Marked event {event['id']} as PUBLISHED in DB.")


if __name__ == "__main__":
    db = MockDatabase()
    broker = MessageBroker()
    order_service = OrderApplicationService(db)
    relay = OutboxRelayWorker(db, broker)

    # 1. Create order: updates DB and creates outbox row in 1 atomic transaction
    print("--- 1. Placing Order with Outbox Pattern ---")
    order_service.place_order("ORD-8821", amount=249.99, customer_id="cust_alex")

    # 2. Background worker polls outbox and safely delivers to message broker
    relay.process_pending_outbox_events()

    # 3. Subsequent poll does not re-publish already published events
    print("\n--- 3. Subsequent Polling Run ---")
    relay.process_pending_outbox_events()
