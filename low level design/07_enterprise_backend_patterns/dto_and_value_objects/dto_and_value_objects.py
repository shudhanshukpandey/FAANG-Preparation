"""DTO and Value Objects: Strict schema boundaries and immutable domain values."""

from dataclasses import dataclass
import re
from typing import Optional


# -------------------------------------------------------------
# 1. Value Object: Immutable and compared by value, not ID
# -------------------------------------------------------------
@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "USD"

    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError("Money amount cannot be negative.")
        if len(self.currency) != 3:
            raise ValueError("Currency must be a 3-letter ISO code.")

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError(f"Cannot add mismatched currencies: {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)


@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self) -> None:
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, self.value):
            raise ValueError(f"Invalid email address syntax: '{self.value}'")


# -------------------------------------------------------------
# 2. DTO (Data Transfer Object): API Boundary Contract
# -------------------------------------------------------------
@dataclass
class UserRegistrationRequestDTO:
    """Simulates a FastAPI Pydantic schema or Django REST serializer."""
    email: str
    full_name: str
    password: str
    initial_credit: float = 0.0
    # Notice: 'is_admin' is intentionally absent to prevent over-posting vulnerabilities!

    @classmethod
    def from_http_payload(cls, json_payload: dict) -> "UserRegistrationRequestDTO":
        # Extracts only declared fields, discarding dangerous injected fields
        return cls(
            email=json_payload["email"],
            full_name=json_payload["full_name"],
            password=json_payload["password"],
            initial_credit=float(json_payload.get("initial_credit", 0.0))
        )


# -------------------------------------------------------------
# 3. Domain Entity: Internal business object
# -------------------------------------------------------------
class UserDomainEntity:
    def __init__(self, user_id: str, email: EmailAddress, balance: Money) -> None:
        self.user_id = user_id
        self.email = email
        self.balance = balance
        self.is_admin = False  # Controlled purely by business rules


if __name__ == "__main__":
    # Test Value Object equality
    m1 = Money(100.0, "USD")
    m2 = Money(100.0, "USD")
    print(f"Are two distinct Money objects equal by value? {m1 == m2}")  # True!

    m3 = m1.add(Money(50.0, "USD"))
    print(f"Money after addition: {m3}")

    # Test DTO protecting against malicious mass assignment
    malicious_payload = {
        "email": "hacker@cyber.io",
        "full_name": "Zero Cool",
        "password": "secret_password",
        "is_admin": True,  # Attacker attempt to elevate privileges!
        "wallet_balance": 9999999.0
    }

    dto = UserRegistrationRequestDTO.from_http_payload(malicious_payload)
    email_vo = EmailAddress(dto.email)
    user = UserDomainEntity("usr_001", email_vo, Money(dto.initial_credit))

    print(f"\nUser created safely: Email={user.email.value}, is_admin={user.is_admin}")
