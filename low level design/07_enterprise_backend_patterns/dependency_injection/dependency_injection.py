"""Dependency Injection: Building a lightweight IoC Container and FastAPI-style Depends engine."""

import inspect
from typing import Callable, Any, Dict, Type


# 1. Services & Components
class AppConfig:
    def __init__(self, db_host: str = "prod.postgres.internal") -> None:
        self.db_host = db_host


class DatabaseConnection:
    def __init__(self, config: AppConfig) -> None:
        self.host = config.db_host
        print(f"[DB] Connected to PostgreSQL at {self.host}")

    def query(self, sql: str) -> list:
        return [{"id": 1, "name": "Alice"}]


class UserRepository:
    def __init__(self, db: DatabaseConnection) -> None:
        self.db = db

    def get_users(self) -> list:
        return self.db.query("SELECT * FROM users;")


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def list_all_active_users(self) -> list:
        return self.repo.get_users()


# 2. Lightweight Dependency Injection Container (Inversion of Control)
class DIContainer:
    def __init__(self) -> None:
        self._singletons: Dict[Type, Any] = {}
        self._factories: Dict[Type, Callable[[], Any]] = {}

    def register_singleton(self, cls: Type, instance: Any) -> None:
        self._singletons[cls] = instance

    def resolve(self, cls: Type) -> Any:
        """Recursively resolves all constructor arguments via type inspection."""
        if cls in self._singletons:
            return self._singletons[cls]

        # Inspect constructor parameters
        sig = inspect.signature(cls.__init__)
        kwargs = {}
        for name, param in sig.parameters.items():
            if name == "self":
                continue
            dep_type = param.annotation
            if dep_type == inspect.Parameter.empty:
                raise ValueError(f"Missing type annotation for '{name}' in {cls.__name__}")
            # Recursively resolve dependency
            kwargs[name] = self.resolve(dep_type)

        return cls(**kwargs)


# 3. FastAPI-style Depends function resolver
def Depends(dependency: Callable[..., Any]):
    """Marker simulating FastAPI's Depends syntax."""
    return dependency


def inject_and_call(handler: Callable[..., Any], container: DIContainer) -> Any:
    """Simulates FastAPI request handler dependency resolution."""
    sig = inspect.signature(handler)
    kwargs = {}
    for name, param in sig.parameters.items():
        if param.annotation != inspect.Parameter.empty:
            kwargs[name] = container.resolve(param.annotation)
    return handler(**kwargs)


# Mock Route Handler
def get_users_route(service: UserService):
    users = service.list_all_active_users()
    return {"status": "success", "data": users}


if __name__ == "__main__":
    container = DIContainer()

    # Configure environment
    container.register_singleton(AppConfig, AppConfig(db_host="localhost:5432"))

    # Resolving UserService automatically builds AppConfig -> DatabaseConnection -> UserRepository -> UserService!
    print("--- Automatic Dependency Graph Resolution ---")
    user_service = container.resolve(UserService)
    print("Resolved UserService instance:", user_service)

    # Simulating FastAPI HTTP request execution
    print("\n--- Route Handler Injected Call ---")
    response = inject_and_call(get_users_route, container)
    print("API Response:", response)
