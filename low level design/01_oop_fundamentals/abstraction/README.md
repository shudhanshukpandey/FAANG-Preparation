# Abstraction

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Abstraction**: The process of hiding internal, low-level implementation details and exposing only essential features to the outside world.
- **Abstraction vs. Encapsulation**:
  - *Abstraction* answers **"What does it do?"** (Focuses on the outside interface).
  - *Encapsulation* answers **"How is it protected?"** (Hiding data/state within boundaries).

## Architecture & Data Flow

```mermaid
sequenceDiagram
    participant Client
    participant CloudStorage
    participant AWS_S3_SDK
    participant Auth_Signature_Engine
    participant TLS_Connection

    Client->>CloudStorage: upload(file_path="report.pdf")
    Note over CloudStorage,TLS_Connection: Internal Complexity Hidden from Client
    CloudStorage->>Auth_Signature_Engine: compute_sha256_signature()
    CloudStorage->>TLS_Connection: open_socket(port=443)
    CloudStorage->>AWS_S3_SDK: put_object(bucket="prod", key="report.pdf")
    CloudStorage-->>Client: returns "https://s3.amazonaws.com/prod/report.pdf"
```

## FAANG Interview Significance
- Simplifies mental models for clients of a library, framework, or microservice.
- Essential for designing clean SDKs, database drivers, and clean API routes.
