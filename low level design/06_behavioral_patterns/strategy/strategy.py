"""Strategy Pattern: Interchangeable payment algorithms selected and switched at runtime."""

from abc import ABC, abstractmethod


# 1. Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


# 2. Concrete Strategy 1: Credit Card
class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str) -> None:
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount: float) -> bool:
        masked = f"****-****-****-{self.card_number[-4:]}"
        print(f"[CreditCard] Charged ${amount:.2f} to {masked}")
        return True


# 3. Concrete Strategy 2: UPI (Unified Payments Interface)
class UPIStrategy(PaymentStrategy):
    def __init__(self, vpa_id: str) -> None:
        self.vpa_id = vpa_id

    def pay(self, amount: float) -> bool:
        print(f"[UPI] Instant debit of ${amount:.2f} via VPA handle '{self.vpa_id}'")
        return True


# 4. Concrete Strategy 3: Crypto Wallet
class CryptoStrategy(PaymentStrategy):
    def __init__(self, wallet_address: str) -> None:
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> bool:
        print(f"[Crypto] Transferred ${amount:.2f} USDT to {self.wallet_address[:8]}... (Tx confirmed)")
        return True


# 5. Context
class CheckoutContext:
    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """Allows switching strategies dynamically at runtime."""
        self._strategy = strategy

    def checkout(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return self._strategy.pay(amount)


if __name__ == "__main__":
    # Client initializes with Credit Card
    cart = CheckoutContext(CreditCardStrategy("4111222233334444", "123"))
    cart.checkout(120.50)

    # User switches payment method to UPI
    print("User switched payment mode to UPI:")
    cart.set_strategy(UPIStrategy("alex@okaxis"))
    cart.checkout(45.00)

    # User switches to Crypto
    print("User switched payment mode to Crypto:")
    cart.set_strategy(CryptoStrategy("0x71C...849"))
    cart.checkout(300.00)
