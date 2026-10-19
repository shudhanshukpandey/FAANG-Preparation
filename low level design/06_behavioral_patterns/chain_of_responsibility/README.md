# Chain of Responsibility Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it or the chain ends.
- **Classification**: Behavioral Pattern.
- **Common Real-World Use Cases**:
  - Web framework middleware pipeline (Auth -> RateLimiter -> BodyValidator -> Handler).
  - ATM cash dispenser (₹2000 note handler -> ₹500 note handler -> ₹100 note handler).
  - Multi-level logging (DEBUG -> INFO -> WARNING -> ERROR).

## Architecture & Data Flow

```mermaid
graph LR
    Request[HTTP Request] --> AuthHandler[Auth Middleware]
    AuthHandler -->|If Valid| RateLimitHandler[Rate Limit Middleware]
    AuthHandler -->|If Invalid| 401[401 Unauthorized]

    RateLimitHandler -->|If Under Limit| RoleHandler[Role/Admin Middleware]
    RateLimitHandler -->|If Exceeded| 429[429 Too Many Requests]

    RoleHandler -->|If Authorized| Controller[Target API Endpoint]
    RoleHandler -->|If Forbidden| 403[403 Forbidden]
```

## FAANG Interview Significance
- The foundation of all backend web middleware in FastAPI, Starlette, Flask, and Django.
- ATM cash dispenser is a classic FAANG machine coding prompt.
