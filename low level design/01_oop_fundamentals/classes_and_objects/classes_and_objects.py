"""Classes & Objects: Demonstrating blueprints, instance vs class state, and methods."""

from typing import ClassVar


class BankAccount:
    # Class variable (shared across all instances)
    bank_name: ClassVar[str] = "Global Prime Bank"
    _interest_rate: ClassVar[float] = 0.04

    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0) -> None:
        # Instance variables (unique to each object instance)
        self.account_number: str = account_number
        self.owner_name: str = owner_name
        self._balance: float = max(0.0, initial_balance)

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient balance.")
        self._balance -= amount
        return self._balance

    def apply_annual_interest(self) -> float:
        accrued = self._balance * self._interest_rate
        self._balance += accrued
        return self._balance

    def get_balance(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"BankAccount(acc={self.account_number!r}, owner={self.owner_name!r}, balance={self._balance:.2f})"


if __name__ == "__main__":
    acc1 = BankAccount("ACC-101", "Alice", 5000.0)
    acc2 = BankAccount("ACC-102", "Bob", 12000.0)

    print(f"Bank: {BankAccount.bank_name}")
    print(f"Initial: {acc1}")
    acc1.deposit(1500)
    print(f"After deposit: {acc1}")
    acc1.withdraw(2000)
    print(f"After withdrawal: {acc1}")
    acc1.apply_annual_interest()
    print(f"After interest: {acc1}")
    print(f"Separate instance intact: {acc2}")
