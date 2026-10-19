"""Decorator Pattern: Dynamic runtime behavior composition via object wrapping."""

from abc import ABC, abstractmethod


# 1. Component Interface
class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# 2. Concrete Components
class Espresso(Beverage):
    def get_description(self) -> str:
        return "Espresso"

    def get_cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def get_description(self) -> str:
        return "House Blend Coffee"

    def get_cost(self) -> float:
        return 0.89


# 3. Base Decorator (Has-A and Is-A Beverage)
class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description()

    def get_cost(self) -> float:
        return self._beverage.get_cost()


# 4. Concrete Decorators (Toppings / Add-ons)
class Milk(BeverageDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Steamed Milk"

    def get_cost(self) -> float:
        return round(self._beverage.get_cost() + 0.40, 2)


class Mocha(BeverageDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Rich Mocha"

    def get_cost(self) -> float:
        return round(self._beverage.get_cost() + 0.60, 2)


class WhipCream(BeverageDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Whipped Cream"

    def get_cost(self) -> float:
        return round(self._beverage.get_cost() + 0.30, 2)


if __name__ == "__main__":
    # Base order: Espresso ($1.99)
    order: Beverage = Espresso()
    print(f"{order.get_description()} = ${order.get_cost():.2f}")

    # Add Milk (+0.40)
    order = Milk(order)
    print(f"{order.get_description()} = ${order.get_cost():.2f}")

    # Add double Mocha (+0.60 + 0.60)
    order = Mocha(order)
    order = Mocha(order)
    print(f"{order.get_description()} = ${order.get_cost():.2f}")

    # Add Whipped Cream (+0.30)
    order = WhipCream(order)
    print(f"Final Custom Drink: {order.get_description()} -> Total: ${order.get_cost():.2f}")
