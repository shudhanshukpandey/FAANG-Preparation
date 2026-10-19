# Data Transfer Objects (DTO) & Value Objects

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Data Transfer Object (DTO)**: An object that carries data between processes or software layers (e.g., from an HTTP JSON request body into a service layer). DTOs contain no business logic—only data fields, typing, and deserialization rules.
  - *FastAPI*: Pydantic schemas (`BaseModel`).
  - *Django*: Django REST Framework Serializers.
  - *Flask*: Marshmallow schemas or Dataclasses.
- **Value Object (Domain-Driven Design)**: An immutable object whose identity is defined strictly by its values rather than an ID.
  - Example: `Money(100, "USD") == Money(100, "USD")` is `True` because their values match. If you have a `$10` bill, you don't care which physical bill it is—its value defines it.

## Architecture & Data Flow

```mermaid
graph LR
    HTTP[HTTP POST JSON Request] -->|Parsed into| RequestDTO[UserCreateDTO (Pydantic / Dataclass)]
    RequestDTO -->|Validated by| Service[UserRegistrationService]
    Service -->|Uses Value Object| VO[EmailAddress Value Object]
    Service -->|Maps to| Domain[User Domain Entity]
    Domain -->|Persists via| Repo[User Database Table]
```

## FAANG Interview Significance
- **Security**: Prevents "Over-posting / Mass Assignment" vulnerabilities (e.g., malicious user sending `is_admin: true` in the HTTP payload).
- **Separation of Concerns**: API contracts can evolve without forcing database migrations.
