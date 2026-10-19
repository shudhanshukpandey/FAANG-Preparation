# Middleware Pipeline (Onion Architecture)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Intercept inbound HTTP requests and outbound HTTP responses in an ordered, layered "onion" pipeline.
- **ASGI & WSGI Standard**:
  - **FastAPI / Starlette**: `app.add_middleware(BaseHTTPMiddleware)`.
  - **Django**: `MIDDLEWARE = ['corsheaders...', 'django.contrib.auth...']`.
  - **Flask**: `@app.before_request` and `@app.after_request` hooks.
- **Core Use Cases**:
  - Request execution timing (`Server-Timing` header).
  - Distributed tracing ID propagation (`X-Request-ID`).
  - Centralized exception mapping and formatting.
  - JWT token verification.

## Architecture & Data Flow

```mermaid
sequenceDiagram
    participant Client
    participant TraceMW as TracingMiddleware (X-Request-ID)
    participant TimeMW as TimingMiddleware
    participant AuthMW as AuthMiddleware
    participant Router as API Endpoint Handler

    Client->>TraceMW: Inbound HTTP Request
    TraceMW->>TimeMW: Attach correlation_id
    TimeMW->>AuthMW: Start timer
    AuthMW->>Router: Verified User Context
    Router-->>AuthMW: Response (200 OK)
    AuthMW-->>TimeMW: Forward Response
    TimeMW-->>TraceMW: Attach 'X-Response-Time: 12ms'
    TraceMW-->>Client: Outbound Response with Headers
```

## FAANG Interview Significance
- Essential for designing scalable API gateways, service meshes, and web frameworks.
- Cleanly decouples cross-cutting concerns from business route logic.
