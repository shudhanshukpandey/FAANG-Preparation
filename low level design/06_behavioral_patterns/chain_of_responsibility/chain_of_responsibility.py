"""Chain of Responsibility Pattern: Middleware filter pipeline and ATM note dispenser."""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any


# 1. Base Handler (Maintains link to next handler in chain)
class RequestHandler(ABC):
    def __init__(self) -> None:
        self._next_handler: Optional["RequestHandler"] = None

    def set_next(self, handler: "RequestHandler") -> "RequestHandler":
        self._next_handler = handler
        return handler  # Returns next handler for fluent builder chaining

    @abstractmethod
    def handle(self, request: Dict[str, Any]) -> bool:
        if self._next_handler:
            return self._next_handler.handle(request)
        return True


# 2. Concrete Filter 1: Authentication
class AuthenticationHandler(RequestHandler):
    def handle(self, request: Dict[str, Any]) -> bool:
        token = request.get("token")
        if not token or token != "VALID_JWT_TOKEN":
            print("[Auth Handler ❌] 401 Unauthorized: Invalid or missing bearer token.")
            return False
        print("[Auth Handler ✅] Token authenticated successfully.")
        return super().handle(request)


# 3. Concrete Filter 2: Rate Limiter
class RateLimitHandler(RequestHandler):
    def __init__(self, max_allowed_per_sec: int) -> None:
        super().__init__()
        self.max_allowed = max_allowed_per_sec

    def handle(self, request: Dict[str, Any]) -> bool:
        rate = request.get("request_rate", 0)
        if rate > self.max_allowed:
            print(f"[RateLimit Handler ❌] 429 Too Many Requests: Rate {rate}/s > limit {self.max_allowed}/s.")
            return False
        print("[RateLimit Handler ✅] Rate within safe threshold.")
        return super().handle(request)


# 4. Concrete Filter 3: Role Authorization
class RoleAuthorizationHandler(RequestHandler):
    def __init__(self, required_role: str) -> None:
        super().__init__()
        self.required_role = required_role

    def handle(self, request: Dict[str, Any]) -> bool:
        user_role = request.get("role")
        if user_role != self.required_role:
            print(f"[Role Handler ❌] 403 Forbidden: User role '{user_role}' lacks required '{self.required_role}'.")
            return False
        print(f"[Role Handler ✅] Access granted for role '{self.required_role}'.")
        return super().handle(request)


if __name__ == "__main__":
    # Assemble the middleware chain
    pipeline = AuthenticationHandler()
    pipeline.set_next(RateLimitHandler(max_allowed_per_sec=10)).set_next(RoleAuthorizationHandler(required_role="ADMIN"))

    print("--- Test 1: Invalid Token ---")
    req1 = {"token": "BAD_TOKEN", "request_rate": 5, "role": "ADMIN"}
    pipeline.handle(req1)

    print("\n--- Test 2: Rate Limit Exceeded ---")
    req2 = {"token": "VALID_JWT_TOKEN", "request_rate": 25, "role": "ADMIN"}
    pipeline.handle(req2)

    print("\n--- Test 3: Insufficient Role ---")
    req3 = {"token": "VALID_JWT_TOKEN", "request_rate": 4, "role": "MEMBER"}
    pipeline.handle(req3)

    print("\n--- Test 4: Fully Valid Request ---")
    req4 = {"token": "VALID_JWT_TOKEN", "request_rate": 2, "role": "ADMIN"}
    success = pipeline.handle(req4)
    print(f"Request reached API controller? {success}")
