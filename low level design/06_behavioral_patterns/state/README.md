# State Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
- **Classification**: Behavioral Pattern.
- **Problem It Solves**: In complex lifecycles (like a Vending Machine, ATM, or Document Review), using `if state == "DRAFT": ... elif state == "PUBLISHED": ...` in every method creates unmaintainable spaghetti code. The State Pattern extracts each state into an independent class.

## Architecture & Data Flow

```mermaid
stateDiagram-v2
    [*] --> IdleState
    IdleState --> HasCoinState : insert_coin()
    HasCoinState --> IdleState : eject_coin()
    HasCoinState --> DispensingState : press_button()
    DispensingState --> IdleState : dispense() [items > 0]
    DispensingState --> SoldOutState : dispense() [items == 0]
```

### Class Diagram
```mermaid
classDiagram
    class VendingMachineState {
        <<interface>>
        +insert_coin(machine: VendingMachine)*
        +eject_coin(machine: VendingMachine)*
        +press_button(machine: VendingMachine)*
        +dispense(machine: VendingMachine)*
    }

    class IdleState {
    }
    class HasCoinState {
    }
    class DispensingState {
    }
    class SoldOutState {
    }

    class VendingMachine {
        -VendingMachineState _current_state
        +set_state(state: VendingMachineState)
    }

    VendingMachineState <|.. IdleState
    VendingMachineState <|.. HasCoinState
    VendingMachineState <|.. DispensingState
    VendingMachineState <|.. SoldOutState
    VendingMachine o-- VendingMachineState
```

## FAANG Interview Significance
- The standard pattern for Finite State Machines (FSM): Vending Machine LLD, Elevator Controller, Turnstile, Order Status Lifecycle.
