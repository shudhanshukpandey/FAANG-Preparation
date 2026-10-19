# Service Layer Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Defines an application's boundary with a layer of services that establishes a set of available operations and coordinates the application's response in each operation.
- **"Skinny Controllers, Fat Services"**:
  - **Controllers (FastAPI routers, Flask blueprints, Django views)**: Strictly handle HTTP serialization, query params, headers, and HTTP status codes (200, 400, 404).
  - **Service Layer**: Orchestrates business rules, validation, domain transactions, security checks, and external side-effects (emails, analytics).

## Architecture & Data Flow

```mermaid
sequenceDiagram
    participant Controller as HTTP Router / Controller
    participant Service as OrderFulfillmentService
    participant InventoryRepo as InventoryRepository
    participant OrderRepo as OrderRepository
    participant Notifier as EventNotifier

    Controller->>Service: place_order(user_id, sku, qty)
    Note over Service: 1. Validate Business Constraints
    Service->>InventoryRepo: get_stock(sku)
    InventoryRepo-->>Service: available: 5

    Note over Service: 2. Execute Domain Calculations
    Service->>InventoryRepo: decrement_stock(sku, qty)
    Service->>OrderRepo: save_order(new_order)
    Service->>Notifier: emit_event("OrderPlaced")
    Service-->>Controller: OrderResultDTO(order_id, status="SUCCESS")
    Controller-->>Controller: serialize JSON -> 201 Created
```

## FAANG Interview Significance
- The central pattern for Clean Architecture / Hexagonal Architecture in backend interviews.
- Separates protocol (HTTP, CLI, WebSockets, gRPC) from pure domain logic.
