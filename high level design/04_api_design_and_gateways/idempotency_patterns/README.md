# Idempotency Patterns in Distributed Systems

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Idempotency Key**: A unique UUID sent in the request header (`Idempotency-Key: <uuid>`).
- **Distributed Lock**: Acquires a lock on the key, executes the transaction, and stores the response.
- **Safe Retries**: If the client retries after a network timeout, the cached response is returned immediately without re-executing payment.
