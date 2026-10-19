"""Composite Pattern: Uniform handling of leaf items and composite tree nodes."""

from abc import ABC, abstractmethod
from typing import List


# 1. Component Interface
class FileSystemItem(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size_kb(self) -> float:
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass


# 2. Leaf (Cannot contain other elements)
class File(FileSystemItem):
    def __init__(self, name: str, size_kb: float) -> None:
        self._name = name
        self._size_kb = size_kb

    def get_name(self) -> str:
        return self._name

    def get_size_kb(self) -> float:
        return self._size_kb

    def display(self, indent: int = 0) -> None:
        spacing = "  " * indent
        print(f"{spacing}📄 {self._name} ({self._size_kb:.1f} KB)")


# 3. Composite (Can contain Leaves and other Composites)
class Directory(FileSystemItem):
    def __init__(self, name: str) -> None:
        self._name = name
        self._children: List[FileSystemItem] = []

    def add(self, item: FileSystemItem) -> None:
        self._children.append(item)

    def remove(self, item: FileSystemItem) -> None:
        self._children.remove(item)

    def get_name(self) -> str:
        return self._name

    def get_size_kb(self) -> float:
        # Recursively aggregate sizes across all leaves and subdirectories
        return sum(child.get_size_kb() for child in self._children)

    def display(self, indent: int = 0) -> None:
        spacing = "  " * indent
        print(f"{spacing}📁 {self._name}/ (Total: {self.get_size_kb():.1f} KB)")
        for child in self._children:
            child.display(indent + 1)


if __name__ == "__main__":
    # Create files
    file1 = File("index.html", 12.5)
    file2 = File("styles.css", 4.2)
    file3 = File("app.js", 25.8)
    secret = File(".env", 0.8)

    # Subdirectory
    src_dir = Directory("src")
    src_dir.add(file1)
    src_dir.add(file2)
    src_dir.add(file3)

    # Root directory containing leaf + subdirectory
    root = Directory("project_root")
    root.add(secret)
    root.add(src_dir)

    # Client treats root directory and individual files uniformly
    root.display()
