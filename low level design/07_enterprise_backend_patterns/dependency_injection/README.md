# Dependency Injection (DI) & Inversion of Control (IoC)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Invert the control of object creation and lifecycle management. Instead of classes instantiating their own dependencies (`self.db = Database()`), dependencies are injected from the outside via constructor or method parameters.
- **FastAPI Core Feature**: `Depends(...)` is FastAPI's native dependency injection engine.
- **Benefits**:
  - Unmatched testability (swap out real Stripe/PostgreSQL for mocks in 1 line).
  - Explicit dependency graph.
  - Lifecycle management (Singleton vs Request-scoped vs Transient).

## Architecture & Data Flow

```mermaid
graph TD
    Container[IoC Container / FastAPI Depends]

    Container -->|Injects| Config[AppConfig (Singleton)]
    Container -->|Injects| DB[DatabaseSession (Request-Scoped)]
    Container -->|Injects| Repo[UserRepository]
    Container -->|Injects| Service[UserService]

    Service --> Endpoint[FastAPI / Flask Route Handler]
```

## FAANG Interview Significance
- How to structure scalable backends so that adding new database connections or caches doesn't require modifying 50 route handlers.
