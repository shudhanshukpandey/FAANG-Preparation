"""Adapter Pattern: Converting incompatible 3rd-party vendor interfaces to a unified interface."""

from abc import ABC, abstractmethod


# 1. Target Interface (What our core application expects)
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount_in_cents: int) -> bool:
        pass


# 2. Adaptee 1: External Legacy Stripe SDK (expects dollars float + currency string)
class StripeLegacySDK:
    def make_charge(self, amount_dollars: float, currency: str) -> dict:
        print(f"[Stripe 3rd-Party SDK] Charged ${amount_dollars:.2f} {currency.upper()}")
        return {"status": "succeeded", "charge_id": "ch_stripe_994"}


# 3. Adaptee 2: External Razorpay SDK (expects rupees, customer_phone, order_id)
class RazorpaySDK:
    def execute_transaction(self, amount_inr: float, order_tag: str) -> dict:
        print(f"[Razorpay 3rd-Party SDK] Paid ₹{amount_inr:.2f} under tag '{order_tag}'")
        return {"code": 200, "txn_id": "rzp_txn_881"}


# 4. Concrete Adapter 1: Adapts Stripe to PaymentProcessor
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_sdk: StripeLegacySDK) -> None:
        self._sdk = stripe_sdk

    def pay(self, amount_in_cents: int) -> bool:
        # Convert cents to dollars required by Stripe SDK
        amount_dollars = amount_in_cents / 100.0
        response = self._sdk.make_charge(amount_dollars, "USD")
        return response.get("status") == "succeeded"


# 5. Concrete Adapter 2: Adapts Razorpay to PaymentProcessor
class RazorpayAdapter(PaymentProcessor):
    def __init__(self, razorpay_sdk: RazorpaySDK) -> None:
        self._sdk = razorpay_sdk

    def pay(self, amount_in_cents: int) -> bool:
        # Currency conversion & mapping
        amount_inr = (amount_in_cents / 100.0) * 83.0  # e.g., 1 USD = 83 INR
        response = self._sdk.execute_transaction(amount_inr, "APP_PURCHASE")
        return response.get("code") == 200


# Client code is completely isolated from vendor specifics
def checkout_cart(processor: PaymentProcessor, total_cents: int) -> None:
    success = processor.pay(total_cents)
    print(f"Cart checkout result: {'Success' if success else 'Failed'}\n")


if __name__ == "__main__":
    total = 2500  # $25.00

    print("--- Checking out with Stripe ---")
    checkout_cart(StripeAdapter(StripeLegacySDK()), total)

    print("--- Checking out with Razorpay ---")
    checkout_cart(RazorpayAdapter(RazorpaySDK()), total)
