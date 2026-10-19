"""Circuit Breaker Pattern: Implementing CLOSED, OPEN, and HALF-OPEN fault tolerance."""

import time
from enum import Enum
from typing import Callable, Any


class CircuitState(Enum):
    CLOSED = "CLOSED"        # Normal traffic passing
    OPEN = "OPEN"            # Failing fast, requests blocked
    HALF_OPEN = "HALF_OPEN"  # Trial probe request allowed


class CircuitBreakerOpenException(Exception):
    pass


class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3, recovery_time_seconds: float = 0.5) -> None:
        self.failure_threshold = failure_threshold
        self.recovery_time_seconds = recovery_time_seconds

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = 0.0

    def call(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        now = time.time()

        # Check if OPEN cooldown has expired -> Transition to HALF_OPEN
        if self.state == CircuitState.OPEN:
            if now - self.last_failure_time >= self.recovery_time_seconds:
                print("[CircuitBreaker] Cooldown elapsed -> Transitioning to HALF-OPEN (Testing probe)")
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerOpenException("Circuit is OPEN! Fast-failing without calling remote API.")

        try:
            result = func(*args, **kwargs)
            # If call succeeded and we were in HALF_OPEN, reset to CLOSED
            if self.state == CircuitState.HALF_OPEN:
                print("[CircuitBreaker] Probe succeeded -> Resetting circuit to CLOSED.")
                self.state = CircuitState.CLOSED
                self.failure_count = 0
            return result
        except Exception as e:
            self._handle_failure()
            raise e

    def _handle_failure(self) -> None:
        self.failure_count += 1
        self.last_failure_time = time.time()
        print(f"[CircuitBreaker] Failure recorded ({self.failure_count}/{self.failure_threshold}).")

        if self.failure_count >= self.failure_threshold or self.state == CircuitState.HALF_OPEN:
            print("[CircuitBreaker ⚠️] Threshold reached -> Tripping circuit to OPEN!")
            self.state = CircuitState.OPEN


# Simulates unreliable 3rd-party Payment Service
class ThirdPartyPaymentAPI:
    def __init__(self) -> None:
        self.is_down = True

    def charge(self, amount: float) -> str:
        if self.is_down:
            raise ConnectionError("503 Service Unavailable")
        return f"Charged ${amount}"


if __name__ == "__main__":
    api = ThirdPartyPaymentAPI()
    breaker = CircuitBreaker(failure_threshold=2, recovery_time_seconds=0.3)

    # 1. Trigger failures until Circuit trips OPEN
    for i in range(1, 4):
        try:
            breaker.call(api.charge, 100.0)
        except Exception as e:
            print(f"Request #{i} failed: {type(e).__name__}")

    # 2. Immediate next call should fail fast without invoking the API!
    print("\n--- Testing Fail-Fast ---")
    try:
        breaker.call(api.charge, 100.0)
    except CircuitBreakerOpenException as e:
        print("Blocked immediately by CircuitBreaker:", e)

    # 3. Wait for cooldown to test HALF-OPEN recovery
    print("\nWaiting for recovery cooldown...")
    time.sleep(0.35)
    api.is_down = False  # Remote service recovered!

    success_result = breaker.call(api.charge, 50.0)
    print("Call result after recovery:", success_result)
    print("Circuit state restored to:", breaker.state.value)
