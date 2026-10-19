"""Repository Pattern: Decoupling domain logic from persistence mechanisms (SQL vs In-Memory)."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional


# 1. Pure Domain Model (Independent of SQLAlchemy or Django ORM)
@dataclass
class User:
    id: str
    email: str
    full_name: str
    is_active: bool = True


# 2. Generic Repository Interface
class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def list_all(self) -> List[User]:
        pass


# 3. Production Implementation (Simulating SQLAlchemy / Django ORM engine)
class SQLUserRepository(UserRepository):
    def __init__(self, db_connection_url: str) -> None:
        self.db_url = db_connection_url
        self._table: Dict[str, User] = {}  # Simulating DB table

    def add(self, user: User) -> None:
        print(f"[SQL Repository -> {self.db_url}] INSERT INTO users (id, email) VALUES ('{user.id}', '{user.email}');")
        self._table[user.id] = user

    def get_by_id(self, user_id: str) -> Optional[User]:
        print(f"[SQL Repository -> {self.db_url}] SELECT * FROM users WHERE id = '{user_id}' LIMIT 1;")
        return self._table.get(user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        print(f"[SQL Repository -> {self.db_url}] SELECT * FROM users WHERE email = '{email}' LIMIT 1;")
        for u in self._table.values():
            if u.email == email:
                return u
        return None

    def list_all(self) -> List[User]:
        return list(self._table.values())


# 4. In-Memory Mock Repository (Instant Pytest unit testing with 0 DB latency)
class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._store: Dict[str, User] = {}

    def add(self, user: User) -> None:
        self._store[user.id] = user

    def get_by_id(self, user_id: str) -> Optional[User]:
        return self._store.get(user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        for u in self._store.values():
            if u.email == email:
                return u
        return None

    def list_all(self) -> List[User]:
        return list(self._store.values())


# 5. Service Consumer (Completely decoupled from SQL vs In-Memory)
class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def register_user(self, user_id: str, email: str, name: str) -> User:
        if self.repo.get_by_email(email):
            raise ValueError(f"User with email '{email}' already registered.")
        user = User(id=user_id, email=email, full_name=name)
        self.repo.add(user)
        return user


if __name__ == "__main__":
    print("--- 1. Production Mode with SQL Repository ---")
    sql_repo = SQLUserRepository("postgresql://prod-db.internal:5432/main")
    service_prod = UserService(sql_repo)
    service_prod.register_user("usr_101", "dev@enterprise.com", "Dev Lead")

    print("\n--- 2. Test Suite Mode with In-Memory Repository (Fast Mocking) ---")
    mock_repo = InMemoryUserRepository()
    service_test = UserService(mock_repo)
    user = service_test.register_user("usr_test_1", "test@test.com", "Tester")
    print(f"Verified registered in mock store: {mock_repo.get_by_id('usr_test_1')}")
