# Law of Demeter (LoD) / Principle of Least Knowledge

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Law of Demeter (LoD)**: Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
- **Rule of Thumb**: "Talk only to your immediate friends; don't talk to strangers."
- **Train Wreck (Anti-Pattern)**: Deep chaining like `order.get_customer().get_profile().get_address().get_zip_code()`. If any intermediate object changes or returns `None`, the whole chain breaks.

## Architecture & Data Flow

```mermaid
sequenceDiagram
    participant Client
    participant Order
    participant Customer
    participant Wallet

    Note over Client,Wallet: Anti-Pattern: Train Wreck Chaining
    Client->>Order: get_customer()
    Order-->>Client: Customer
    Client->>Customer: get_wallet()
    Customer-->>Client: Wallet
    Client->>Wallet: deduct_funds(100)

    Note over Client,Wallet: Refactored: Tell, Don't Ask (Demeter Compliant)
    Client->>Order: process_payment(100)
    Order->>Customer: charge(100)
    Customer->>Wallet: deduct(100)
    Order-->>Client: success confirmation
```

## Demeter Guidelines (Methods a function may call):
An object `M` of class `C` may only invoke methods of:
1. `C` itself.
2. An object created by `M`.
3. Any arguments passed to `M`.
4. Any object held in an instance variable of `C`.

## FAANG Interview Significance
- Enforces loose coupling and prevents fragile unit tests where every mock needs 5 layers of child mocks.
- "Tell, Don't Ask" mindset in domain-driven design.
