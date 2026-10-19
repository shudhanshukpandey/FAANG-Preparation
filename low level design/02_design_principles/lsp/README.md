# Liskov Substitution Principle (LSP)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Definition**: "Subtypes must be substitutable for their base types without altering the correctness of the program." (Formulated by Barbara Liskov).
- **Rule of Thumb**: If class `B` is a subtype of class `A`, we should be able to pass an object of `B` anywhere `A` is expected, and the program should continue working correctly.
- **Classic LSP Violations**:
  1. **The Square-Rectangle Problem**: Subclassing `Square` from `Rectangle` and overriding `set_width()` to also set height breaks code expecting independent width and height behavior.
  2. **The Non-flying Bird**: `Penguin` inherits `Bird` which has `fly()`, but `Penguin.fly()` raises `NotImplementedError("Penguins can't fly!")`.

## Architecture & Data Flow

```mermaid
classDiagram
    subgraph LSP_Violation [Anti-Pattern: Breaks Substitution]
        class Bird {
            +fly()
        }
        class Penguin {
            +fly() throws Exception!
        }
        Bird <|-- Penguin
    end

    subgraph LSP_Refactored [Refactored Hierarchy]
        class Animal {
            +move()
        }
        class FlyingBird {
            +fly()
        }
        class SwimmingBird {
            +swim()
        }
        Animal <|-- FlyingBird
        Animal <|-- SwimmingBird
    end
```

## 4 Formal Rules of LSP
1. **Preconditions cannot be strengthened** in a subtype (don't demand more inputs than base class).
2. **Postconditions cannot be weakened** in a subtype (don't guarantee less output than base class).
3. **Invariants of the supertype must be preserved**.
4. **History constraint**: Methods must not modify state in ways supertype methods wouldn't.
