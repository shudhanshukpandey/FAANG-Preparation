# Dependency Inversion Principle (DIP)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Definition**:
  1. "High-level modules should not depend upon low-level modules. Both should depend upon abstractions."
  2. "Abstractions should not depend upon details. Details should depend upon abstractions."
- **Inversion of Control (IoC)**: High-level business logic is no longer tightly coupled to concrete databases, network clients, or disk I/O.
- **The Anti-Pattern**: High-level `OrderService` directly instantiating `PostgresConnection()` and `StripeClient()` in its constructor.

## Architecture & Data Flow

```mermaid
graph TD
    subgraph TightCoupling [Anti-Pattern: High-Level Depends on Low-Level]
        OrderServiceTight[OrderService (High-level)] --> PostgresDB[PostgresDB (Low-level)]
        OrderServiceTight --> StripeAPI[StripeAPI (Low-level)]
    end

    subgraph DependencyInverted [DIP Compliant: Both Depend on Abstractions]
        OrderServiceDIP[OrderService (High-level)] --> IDatabase[<<interface>> IDatabase]
        OrderServiceDIP --> IPaymentGateway[<<interface>> IPaymentGateway]

        PostgresDBImpl[PostgresDB] -.->|implements| IDatabase
        MongoTestDBImpl[Mongo / In-Memory Mock] -.->|implements| IDatabase

        StripeGatewayImpl[StripeGateway] -.->|implements| IPaymentGateway
        PayPalGatewayImpl[PayPalGateway] -.->|implements| IPaymentGateway
    end
```

## FAANG Interview Significance
- Essential for unit testing with pytest (easily passing in-memory mocks without standing up actual PostgreSQL/Stripe servers).
- FastAPI's core philosophy with `Depends()`.
