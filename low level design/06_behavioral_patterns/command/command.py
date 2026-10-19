"""Command Pattern: Encapsulating requests as objects with reversible Undo/Redo."""

from abc import ABC, abstractmethod
from typing import List


# 1. Receiver
class SmartLight:
    def __init__(self, room_name: str) -> None:
        self.room_name = room_name
        self.is_on: bool = False
        self.brightness: int = 0

    def turn_on(self) -> None:
        self.is_on = True
        self.brightness = 100
        print(f"[{self.room_name} Light] Switched ON (100% brightness).")

    def turn_off(self) -> None:
        self.is_on = False
        self.brightness = 0
        print(f"[{self.room_name} Light] Switched OFF.")

    def set_brightness(self, level: int) -> None:
        self.brightness = level
        print(f"[{self.room_name} Light] Dimmed to {level}%.")


# 2. Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


# 3. Concrete Commands
class TurnOnCommand(Command):
    def __init__(self, light: SmartLight) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.turn_on()

    def undo(self) -> None:
        self._light.turn_off()


class DimCommand(Command):
    def __init__(self, light: SmartLight, new_level: int) -> None:
        self._light = light
        self._new_level = new_level
        self._prev_level = 0

    def execute(self) -> None:
        self._prev_level = self._light.brightness
        self._light.set_brightness(self._new_level)

    def undo(self) -> None:
        print(f"Reverting brightness back to previous {self._prev_level}%...")
        self._light.set_brightness(self._prev_level)


# 4. Invoker: Remote Control maintaining command history stack for undo
class RemoteControlInvoker:
    def __init__(self) -> None:
        self._history: List[Command] = []

    def press_button(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def press_undo(self) -> None:
        if not self._history:
            print("[Invoker] No commands to undo.")
            return
        last_command = self._history.pop()
        last_command.undo()


if __name__ == "__main__":
    living_room_light = SmartLight("Living Room")
    remote = RemoteControlInvoker()

    # Turn On
    turn_on = TurnOnCommand(living_room_light)
    remote.press_button(turn_on)

    # Dim to 40%
    dim = DimCommand(living_room_light, 40)
    remote.press_button(dim)

    # Undo dimming -> restores 100%
    print("\n--- Undoing Last Action ---")
    remote.press_undo()

    # Undo turning on -> turns off
    print("\n--- Undoing Another Action ---")
    remote.press_undo()
