"""Interfaces and Protocols: Comparing abc.ABC (Nominal) and typing.Protocol (Structural)."""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# 1. Nominal Interface using abc.ABC
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process charge of amount."""
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        """Issue refund for transaction."""
        pass


class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"[Stripe] Charged ${amount:.2f} successfully.")
        return True

    def refund(self, transaction_id: str) -> bool:
        print(f"[Stripe] Refunded transaction: {transaction_id}")
        return True


# 2. Structural Subtyping using typing.Protocol (Duck Typing with type safety)
@runtime_checkable
class NotificationSender(Protocol):
    def send_message(self, recipient: str, message: str) -> bool:
        ...


# Note: SlackNotifier does NOT explicitly inherit NotificationSender!
class SlackNotifier:
    def send_message(self, recipient: str, message: str) -> bool:
        print(f"[Slack] Sent message to #{recipient}: {message}")
        return True


# Consumer depends strictly on abstractions
class CheckoutService:
    def __init__(self, payment_gateway: PaymentGateway, notifier: NotificationSender) -> None:
        self.gateway = payment_gateway
        self.notifier = notifier

    def checkout(self, customer_channel: str, amount: float) -> bool:
        success = self.gateway.process_payment(amount)
        if success:
            self.notifier.send_message(customer_channel, f"Payment of ${amount:.2f} confirmed!")
        return success


if __name__ == "__main__":
    stripe = StripeGateway()
    slack = SlackNotifier()

    # Runtime checkable protocol verification
    print(f"Does SlackNotifier conform to NotificationSender? {isinstance(slack, NotificationSender)}")

    service = CheckoutService(payment_gateway=stripe, notifier=slack)
    service.checkout("orders-alerts", 199.99)
