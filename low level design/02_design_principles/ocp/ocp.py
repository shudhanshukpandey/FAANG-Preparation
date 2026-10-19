"""Open/Closed Principle (OCP): Extending functionality by adding new classes without modifying existing ones."""

from abc import ABC, abstractmethod


# -------------------------------------------------------------
# Anti-Pattern: Violating OCP via if/elif/else branch modification
# -------------------------------------------------------------
class DiscountCalculatorViolating:
    def calculate(self, customer_type: str, price: float) -> float:
        # Every time a new tier (e.g. "STUDENT", "FESTIVAL") is added, this code MUST be modified!
        if customer_type == "REGULAR":
            return price
        elif customer_type == "SILVER":
            return price * 0.90
        elif customer_type == "GOLD":
            return price * 0.80
        elif customer_type == "PLATINUM":
            return price * 0.70
        else:
            raise ValueError(f"Unknown tier: {customer_type}")


# -------------------------------------------------------------
# Clean Refactor: OCP Compliant via Strategy Abstraction
# -------------------------------------------------------------
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price


class GoldDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return round(price * 0.80, 2)


# New requirement: Add VIP / Festival discount without touching ANY existing class!
class FestivalSpecialDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return round(price * 0.65, 2)  # 35% discount for festival


class OrderCheckout:
    """Closed for modification: Never needs editing when discount policies change."""
    @staticmethod
    def compute_final_price(price: float, discount: DiscountStrategy) -> float:
        return discount.calculate(price)


if __name__ == "__main__":
    base_price = 200.0

    print("Regular Checkout:", OrderCheckout.compute_final_price(base_price, RegularDiscount()))
    print("Gold Tier Checkout:", OrderCheckout.compute_final_price(base_price, GoldDiscount()))
    # Extended smoothly without modifying OrderCheckout:
    print("Festival Special Checkout:", OrderCheckout.compute_final_price(base_price, FestivalSpecialDiscount()))
