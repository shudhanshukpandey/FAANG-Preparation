# Rate Limiter Service (Machine Coding)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Problem**: Design an end-to-end, production-ready Rate Limiter Service that can be applied to backend endpoints (FastAPI / Flask / Django).
- **Core Requirements**:
  1. Configurable limits based on User Tier (e.g., `FREE`: 5 req/min, `PRO`: 100 req/min).
  2. Sliding Window Counter / Log algorithm.
  3. Standard HTTP Rate Limit headers:
     - `X-RateLimit-Limit`
     - `X-RateLimit-Remaining`
     - `X-RateLimit-Reset`
  4. Non-intrusive Python function/route decorator (`@rate_limit`).

## Architecture & Data Flow

```mermaid
sequenceDiagram
    participant Client
    participant Limiter as RateLimiterDecorator
    participant Storage as In-Memory / Redis Storage
    participant Handler as Route Handler

    Client->>Limiter: HTTP Request (API-Key: 'pro_key_99')
    Limiter->>Storage: get_timestamps(key)
    Storage-->>Limiter: [171000001, 171000002]

    alt Request Within Limit
        Limiter->>Storage: append_timestamp(now)
        Limiter->>Handler: invoke endpoint
        Handler-->>Limiter: 200 OK Response
        Limiter-->>Client: 200 OK + RateLimit Headers
    else Limit Exceeded
        Limiter-->>Client: 429 Too Many Requests (Retry-After: 15s)
    end
```

## FAANG Interview Significance
- Evaluates both algorithmic precision (sliding window calculation) and software architecture (decorators, middleware integration, header standards).
