"""Encapsulation: Enforcing data integrity using private variables, name mangling, and @property."""

import hashlib


class DigitalWallet:
    def __init__(self, owner: str, initial_deposit: float, pin: str) -> None:
        self.owner: str = owner                    # Public
        self._currency: str = "USD"               # Protected by convention
        self._balance: float = initial_deposit    # Protected
        self.__pin_hash: str = self._hash(pin)    # Private (Name mangled to _DigitalWallet__pin_hash)

    def _hash(self, pin: str) -> str:
        return hashlib.sha256(pin.encode("utf-8")).hexdigest()

    def _verify_pin(self, pin: str) -> bool:
        return self._hash(pin) == self.__pin_hash

    # Managed attribute via @property (Encapsulated Getter)
    @property
    def balance(self) -> float:
        """Read-only access to balance."""
        return self._balance

    # Controlled mutators with domain validation
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be strictly positive.")
        self._balance += amount

    def withdraw(self, amount: float, pin: str) -> bool:
        if not self._verify_pin(pin):
            raise PermissionError("Invalid PIN.")
        if amount <= 0:
            raise ValueError("Withdrawal must be strictly positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return True


if __name__ == "__main__":
    wallet = DigitalWallet(owner="Alice", initial_deposit=1000.0, pin="1234")
    print(f"Owner: {wallet.owner}, Balance: ${wallet.balance:.2f}")

    wallet.deposit(500)
    print(f"After deposit: ${wallet.balance:.2f}")

    # Protected mutation via method
    wallet.withdraw(300, pin="1234")
    print(f"After withdrawal: ${wallet.balance:.2f}")

    # Demonstrating name mangling protection
    try:
        # Direct access fails with AttributeError
        print(wallet.__pin_hash)
    except AttributeError:
        print("Direct access to __pin_hash correctly failed due to private name mangling.")
