"""Liskov Substitution Principle (LSP): Ensuring subtypes strictly honor supertype contracts."""

from abc import ABC, abstractmethod


# -------------------------------------------------------------
# Anti-Pattern: Square inheriting Rectangle (Violates LSP)
# -------------------------------------------------------------
class RectangleViolating:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height: float) -> None:
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class SquareViolating(RectangleViolating):
    def set_width(self, width: float) -> None:
        self.width = width
        self.height = width  # Side effect breaks rectangle expectations!

    def set_height(self, height: float) -> None:
        self.width = height
        self.height = height


def resize_and_verify_area(rect: RectangleViolating) -> bool:
    """Client function expecting standard Rectangle behavior."""
    rect.set_width(5)
    rect.set_height(4)
    # Rectangle contract expects: width(5) * height(4) = 20
    return rect.area() == 20


# -------------------------------------------------------------
# Clean Refactor: Independent Shape Abstractions
# -------------------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


if __name__ == "__main__":
    # Demonstrating the violation:
    reg_rect = RectangleViolating(2, 3)
    sq_viol = SquareViolating(2, 2)

    print("Rectangle passes contract?", resize_and_verify_area(reg_rect))  # True
    print("Square passes contract?", resize_and_verify_area(sq_viol))     # False! (4*4=16 != 20)

    # Clean polymorphic shapes honoring contracts:
    shapes = [Rectangle(5, 4), Square(4)]
    print("Clean polymorphic areas:", [s.area() for s in shapes])
