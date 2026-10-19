# UML Sequence Diagram

## Overview
A **Sequence Diagram** is an interaction diagram that details how operations are carried out over time. It captures:
- **Lifelines**: Objects/actors participating in the interaction over a vertical timeline.
- **Activation Boxes**: Periods during which an object is executing an operation.
- **Synchronous Calls (`->>`)**: Caller waits for the callee to return.
- **Asynchronous Calls (`-x`)**: Fire-and-forget message passing.
- **Return Messages (`-->>`)**: Value or control returned to the caller.
- **Frames**: `alt` (conditional branching), `loop` (iterations), and `opt` (optional steps).

## Architecture & Data Flow: Order Checkout Flow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Router as API Gateway / Router
    participant Service as OrderService
    participant Inventory as InventoryService
    participant Payment as PaymentGateway
    participant DB as Postgres Database

    User->>Router: POST /api/v1/orders (cart_id, card_token)
    activate Router
    Router->>Service: create_order(user_id, cart_id)
    activate Service

    Service->>Inventory: lock_inventory(items)
    activate Inventory
    Inventory-->>Service: reservation_success: true
    deactivate Inventory

    alt Payment Succeeded
        Service->>Payment: charge(amount, card_token)
        activate Payment
        Payment-->>Service: status: 200 (txn_id)
        deactivate Payment

        Service->>DB: save_order(status="CONFIRMED")
        activate DB
        DB-->>Service: order_record
        deactivate DB

        Service-->>Router: OrderDTO (status="CONFIRMED")
        Router-->>User: 201 Created (Order Details)
    else Payment Failed
        Service->>Inventory: release_inventory(items)
        Service-->>Router: Error("Payment Declined")
        Router-->>User: 402 Payment Required
    end

    deactivate Service
    deactivate Router
```

## FAANG LLD Interview Tips
- The sequence diagram is the most requested diagram when explaining the runtime data flow in machine coding rounds.
- Focus on happy path first, then show error/rollback flows in `alt` blocks.
