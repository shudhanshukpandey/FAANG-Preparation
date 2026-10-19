"""State Pattern: Modeling a Vending Machine Finite State Machine (FSM)."""

from abc import ABC, abstractmethod


# Forward declaration
class VendingMachine:
    pass


# 1. State Interface
class VendingState(ABC):
    @abstractmethod
    def insert_coin(self, machine: "VendingMachine") -> None:
        pass

    @abstractmethod
    def eject_coin(self, machine: "VendingMachine") -> None:
        pass

    @abstractmethod
    def press_button(self, machine: "VendingMachine") -> None:
        pass

    @abstractmethod
    def dispense(self, machine: "VendingMachine") -> None:
        pass


# 2. Context: Vending Machine
class VendingMachine:
    def __init__(self, item_count: int) -> None:
        self.item_count = item_count
        # States
        self.idle_state = IdleState()
        self.has_coin_state = HasCoinState()
        self.dispensing_state = DispensingState()
        self.sold_out_state = SoldOutState()

        self._state: VendingState = self.idle_state if item_count > 0 else self.sold_out_state

    def set_state(self, state: VendingState) -> None:
        self._state = state

    # Delegates actions to active state
    def insert_coin(self) -> None:
        self._state.insert_coin(self)

    def eject_coin(self) -> None:
        self._state.eject_coin(self)

    def press_button(self) -> None:
        self._state.press_button(self)
        self._state.dispense(self)


# 3. Concrete States
class IdleState(VendingState):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("[Idle] Coin accepted. Transitioning to HasCoin state.")
        machine.set_state(machine.has_coin_state)

    def eject_coin(self, machine: VendingMachine) -> None:
        print("[Idle] No coin to eject.")

    def press_button(self, machine: VendingMachine) -> None:
        print("[Idle] Please insert a coin first.")

    def dispense(self, machine: VendingMachine) -> None:
        pass


class HasCoinState(VendingState):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("[HasCoin] Coin already inserted.")

    def eject_coin(self, machine: VendingMachine) -> None:
        print("[HasCoin] Coin returned. Returning to Idle state.")
        machine.set_state(machine.idle_state)

    def press_button(self, machine: VendingMachine) -> None:
        print("[HasCoin] Button pressed. Transitioning to Dispensing state.")
        machine.set_state(machine.dispensing_state)

    def dispense(self, machine: VendingMachine) -> None:
        pass


class DispensingState(VendingState):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("[Dispensing] Please wait, dispensing current item.")

    def eject_coin(self, machine: VendingMachine) -> None:
        print("[Dispensing] Cannot eject coin during dispensing.")

    def press_button(self, machine: VendingMachine) -> None:
        print("[Dispensing] Item is already being dispensed.")

    def dispense(self, machine: VendingMachine) -> None:
        machine.item_count -= 1
        print(f"[Dispensing] Successfully dispensed soda! Items remaining: {machine.item_count}")
        if machine.item_count > 0:
            machine.set_state(machine.idle_state)
        else:
            print("[Dispensing] Machine is now SOLD OUT!")
            machine.set_state(machine.sold_out_state)


class SoldOutState(VendingState):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("[SoldOut] Cannot accept coin. Machine is empty.")

    def eject_coin(self, machine: VendingMachine) -> None:
        print("[SoldOut] No coin to eject.")

    def press_button(self, machine: VendingMachine) -> None:
        print("[SoldOut] Out of stock.")

    def dispense(self, machine: VendingMachine) -> None:
        pass


if __name__ == "__main__":
    machine = VendingMachine(item_count=1)

    print("--- 1. Purchase Item ---")
    machine.insert_coin()
    machine.press_button()

    print("\n--- 2. Try purchasing when Sold Out ---")
    machine.insert_coin()
    machine.press_button()
