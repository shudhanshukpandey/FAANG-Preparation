"""Prototype Pattern: Creating new objects by cloning pre-configured prototypes."""

from abc import ABC, abstractmethod
import copy
from typing import Dict, Any


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype":
        pass


class GameUnit(Prototype):
    def __init__(self, unit_type: str, health: int, stats: Dict[str, Any]) -> None:
        self.unit_type = unit_type
        self.health = health
        self.stats = stats  # Nested dictionary (requires deepcopy!)

    def clone(self) -> "GameUnit":
        # Deepcopy ensures nested dictionaries and lists are not shared between clones
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"GameUnit(type={self.unit_type!r}, health={self.health}, stats={self.stats})"


class UnitRegistry:
    """Registry maintaining pre-configured prototype instances."""
    def __init__(self) -> None:
        self._prototypes: Dict[str, GameUnit] = {}

    def register(self, key: str, prototype: GameUnit) -> None:
        self._prototypes[key] = prototype

    def spawn(self, key: str) -> GameUnit:
        if key not in self._prototypes:
            raise KeyError(f"Prototype '{key}' not registered.")
        return self._prototypes[key].clone()


if __name__ == "__main__":
    registry = UnitRegistry()

    # Pre-configure expensive prototype
    warrior_prototype = GameUnit(
        unit_type="EliteWarrior",
        health=500,
        stats={"armor": 80, "attack_power": 120, "weapon": "Broadsword"}
    )
    registry.register("warrior", warrior_prototype)

    # Spawn two independent instances
    unit1 = registry.spawn("warrior")
    unit2 = registry.spawn("warrior")

    # Modify unit1 without affecting unit2 or the prototype
    unit1.health -= 150
    unit1.stats["weapon"] = "Flaming Sword"

    print("Unit 1 (damaged, upgraded weapon):", unit1)
    print("Unit 2 (unaffected, pristine clone):", unit2)
