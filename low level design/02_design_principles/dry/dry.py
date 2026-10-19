"""DRY Principle: Eliminating duplicated business logic with centralized, reusable services."""

from dataclasses import dataclass
from typing import List


# -------------------------------------------------------------
# Anti-Pattern: WET (Duplicated tax & validation logic)
# -------------------------------------------------------------
class InvoicingServiceWET:
    def create_invoice(self, subtotal: float, state: str) -> float:
        # Duplicated tax calculation
        tax_rate = 0.08 if state == "CA" else 0.05
        tax = subtotal * tax_rate
        total = subtotal + tax
        return total


class CheckoutServiceWET:
    def process_cart(self, subtotal: float, state: str) -> float:
        # Same calculation duplicated! If CA tax updates to 0.09, this might get forgotten!
        tax_rate = 0.08 if state == "CA" else 0.05
        tax = subtotal * tax_rate
        total = subtotal + tax
        return total


# -------------------------------------------------------------
# Clean Refactor: Single Source of Truth for Tax Calculation
# -------------------------------------------------------------
class TaxPolicy:
    STATE_RATES = {
        "CA": 0.085,
        "NY": 0.088,
        "TX": 0.0625,
    }
    DEFAULT_RATE = 0.05

    @classmethod
    def calculate_tax(cls, amount: float, state: str) -> float:
        rate = cls.STATE_RATES.get(state.upper(), cls.DEFAULT_RATE)
        return round(amount * rate, 2)


class PricingService:
    @staticmethod
    def compute_final_price(subtotal: float, state: str, discount: float = 0.0) -> float:
        discounted = max(0.0, subtotal - discount)
        tax = TaxPolicy.calculate_tax(discounted, state)
        return discounted + tax


class InvoicingService:
    def __init__(self, pricing_service: PricingService) -> None:
        self.pricing = pricing_service

    def create_invoice(self, subtotal: float, state: str) -> float:
        return self.pricing.compute_final_price(subtotal, state)


class CheckoutService:
    def __init__(self, pricing_service: PricingService) -> None:
        self.pricing = pricing_service

    def process_cart(self, subtotal: float, state: str) -> float:
        return self.pricing.compute_final_price(subtotal, state)


if __name__ == "__main__":
    pricing = PricingService()
    invoice_svc = InvoicingService(pricing)
    checkout_svc = CheckoutService(pricing)

    print(f"Invoice for $100 in CA: ${invoice_svc.create_invoice(100.0, 'CA'):.2f}")
    print(f"Cart for $100 in CA: ${checkout_svc.process_cart(100.0, 'CA'):.2f}")
