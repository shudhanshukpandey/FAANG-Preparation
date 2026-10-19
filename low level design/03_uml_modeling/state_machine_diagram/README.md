# UML State Machine Diagram

## Overview
A **State Machine Diagram** (or Statechart) models the lifecycle of an object as it transitions through various states in response to internal or external events.
- **State**: Condition or situation in the life of an object during which it satisfies some condition or performs an activity.
- **Transition**: Relationship between two states triggered by an event.
- **Guard Condition `[condition]`**: Boolean expression that must be true for the transition to fire.
- **Action `/ action()`**: Operation executed during state transition.

## Architecture & Data Flow: Order State Machine

```mermaid
stateDiagram-v2
    [*] --> DRAFT : User adds items to cart
    DRAFT --> PENDING_PAYMENT : checkout_clicked()
    
    PENDING_PAYMENT --> PAID : payment_successful() / generate_invoice()
    PENDING_PAYMENT --> PAYMENT_FAILED : payment_declined()
    PAYMENT_FAILED --> PENDING_PAYMENT : retry_payment()
    PAYMENT_FAILED --> CANCELLED : timeout_15_mins()

    PAID --> PROCESSING : assign_warehouse()
    PROCESSING --> SHIPPED : courier_pickup() / dispatch_tracking_sms()
    SHIPPED --> OUT_FOR_DELIVERY : reached_local_hub()
    OUT_FOR_DELIVERY --> DELIVERED : customer_signature_confirmed()

    PROCESSING --> CANCELLED : user_cancel_request() / issue_refund()
    DELIVERED --> RETURNED : return_requested() [within 7 days] / schedule_pickup()

    CANCELLED --> [*]
    DELIVERED --> [*]
    RETURNED --> [*]
```

## Direct Connection to Design Patterns
- State Machine Diagrams directly translate into the **State Design Pattern** in code.
- Rather than messy nested `if order.status == "PENDING": elif order.status == "PAID": ...`, each state becomes a dedicated class encapsulating valid state transitions.
