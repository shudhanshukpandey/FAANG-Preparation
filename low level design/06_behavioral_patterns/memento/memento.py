"""Memento Pattern: State snapshot and rollback for text editor undo mechanism."""

from dataclasses import dataclass
from typing import List


# 1. Memento: Immutable state container
@dataclass(frozen=True)
class EditorMemento:
    content: str
    cursor_position: int


# 2. Originator: Creates and restores from its own internal memento
class TextEditor:
    def __init__(self) -> None:
        self._content: str = ""
        self._cursor: int = 0

    def type_text(self, text: str) -> None:
        self._content += text
        self._cursor = len(self._content)

    def save(self) -> EditorMemento:
        """Creates an immutable snapshot of current state."""
        return EditorMemento(content=self._content, cursor_position=self._cursor)

    def restore(self, memento: EditorMemento) -> None:
        """Restores state from memento without violating encapsulation."""
        self._content = memento.content
        self._cursor = memento.cursor_position
        print(f"[Editor] Restored state to: '{self._content}' (Cursor at {self._cursor})")

    def __repr__(self) -> str:
        return f"TextEditor(content={self._content!r}, cursor={self._cursor})"


# 3. Caretaker: Manages history stack
class HistoryCaretaker:
    def __init__(self, editor: TextEditor) -> None:
        self._editor = editor
        self._history: List[EditorMemento] = []

    def backup(self) -> None:
        snapshot = self._editor.save()
        self._history.append(snapshot)

    def undo(self) -> None:
        if not self._history:
            print("[History] Nothing to undo.")
            return
        last_snapshot = self._history.pop()
        self._editor.restore(last_snapshot)


if __name__ == "__main__":
    editor = TextEditor()
    history = HistoryCaretaker(editor)

    # State 1: "Design "
    editor.type_text("Design ")
    history.backup()

    # State 2: "Design Patterns "
    editor.type_text("Patterns ")
    history.backup()

    # State 3: "Design Patterns are awesome!"
    editor.type_text("are awesome!")
    print("Current State:", editor)

    # Undo 1
    print("\n--- Undo Step 1 ---")
    history.undo()
    print("After 1st Undo:", editor)

    # Undo 2
    print("\n--- Undo Step 2 ---")
    history.undo()
    print("After 2nd Undo:", editor)
