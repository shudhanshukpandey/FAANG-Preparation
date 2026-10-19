"""Flyweight Pattern: Drastically reducing memory footprint by sharing intrinsic state."""

from typing import Dict, List


# 1. Flyweight: Stores heavy, immutable Intrinsic state
class TreeType:
    def __init__(self, name: str, color: str, texture_bytes: str) -> None:
        self.name = name
        self.color = color
        self.texture_bytes = texture_bytes  # Simulates heavy asset (e.g. 50 KB sprite)

    def draw(self, x: int, y: int) -> None:
        # Extrinsic state (x, y coordinates) passed from outside
        print(f"Rendered '{self.name}' ({self.color}) at ({x}, {y}) using shared texture.")


# 2. Flyweight Factory: Caches and reuses intrinsic TreeType instances
class TreeFactory:
    _tree_types: Dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture_bytes: str) -> TreeType:
        key = f"{name}_{color}"
        if key not in cls._tree_types:
            print(f"[TreeFactory] Creating NEW heavy TreeType flyweight for '{key}'")
            cls._tree_types[key] = TreeType(name, color, texture_bytes)
        return cls._tree_types[key]

    @classmethod
    def total_flyweights(cls) -> int:
        return len(cls._tree_types)


# 3. Context: Contains unique extrinsic state (coordinates) and reference to shared flyweight
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self.x = x
        self.y = y
        self.tree_type = tree_type  # Lightweight reference

    def draw(self) -> None:
        self.tree_type.draw(self.x, self.y)


# 4. Client / Forest Manager
class Forest:
    def __init__(self) -> None:
        self.trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)


if __name__ == "__main__":
    forest = Forest()

    # Planting 1,000 Oak trees and 1,000 Pine trees
    for i in range(5):
        forest.plant_tree(x=i * 10, y=i * 20, name="Oak", color="Green", texture="OakMesh_50KB")
    for i in range(5):
        forest.plant_tree(x=i * 15, y=i * 30, name="Pine", color="DarkGreen", texture="PineMesh_45KB")

    print(f"\nTotal Tree instances planted in Forest: {len(forest.trees)}")
    print(f"Total heavy TreeType objects stored in RAM: {TreeFactory.total_flyweights()}")

    # Render sample trees
    forest.trees[0].draw()
    forest.trees[6].draw()
