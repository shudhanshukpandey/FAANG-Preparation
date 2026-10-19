"""Dependency Inversion Principle (DIP): Inverting dependencies to interfaces for loose coupling."""

from abc import ABC, abstractmethod


# -------------------------------------------------------------
# Anti-Pattern: High-level directly instantiating low-level dependencies
# -------------------------------------------------------------
class MySQLDatabase:
    def insert(self, record: str) -> None:
        print(f"[MySQL] INSERT INTO orders VALUES ('{record}')")


class OrderServiceTightCoupled:
    def __init__(self) -> None:
        # High-level domain service is tightly coupled to concrete MySQL implementation!
        # Cannot be unit tested without a running MySQL instance!
        self.db = MySQLDatabase()

    def create_order(self, order_id: str) -> None:
        self.db.insert(order_id)


# -------------------------------------------------------------
# Clean Refactor: Both depend upon abstractions
# -------------------------------------------------------------
class OrderRepository(ABC):
    @abstractmethod
    def save(self, order_id: str, payload: dict) -> None:
        pass


# Concrete low-level implementation 1 (Production SQL)
class PostgresOrderRepository(OrderRepository):
    def save(self, order_id: str, payload: dict) -> None:
        print(f"[PostgreSQL Engine] Persisted order #{order_id} to cluster.")


# Concrete low-level implementation 2 (In-Memory for Fast Unit Tests)
class InMemoryOrderRepository(OrderRepository):
    def __init__(self) -> None:
        self.storage: dict = {}

    def save(self, order_id: str, payload: dict) -> None:
        self.storage[order_id] = payload
        print(f"[InMemory Test Store] Mocked persistence of order #{order_id}.")


# High-level domain service depends strictly on OrderRepository interface
class OrderService:
    def __init__(self, repo: OrderRepository) -> None:
        # Injected dependency
        self.repo = repo

    def place_order(self, order_id: str, payload: dict) -> None:
        print(f"Executing business validation for Order #{order_id}...")
        self.repo.save(order_id, payload)


if __name__ == "__main__":
    # In production: Inject PostgreSQL
    prod_service = OrderService(repo=PostgresOrderRepository())
    prod_service.place_order("ORD-PROD-99", {"amount": 250.0})

    print("-" * 50)

    # In unit tests: Inject lightweight In-Memory Repo with zero network calls
    test_repo = InMemoryOrderRepository()
    test_service = OrderService(repo=test_repo)
    test_service.place_order("ORD-TEST-01", {"amount": 50.0})
    print(f"Verified test storage contents: {test_repo.storage}")
