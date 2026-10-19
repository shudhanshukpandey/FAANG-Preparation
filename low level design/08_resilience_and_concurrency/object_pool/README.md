# Object Pool Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Manage the caching and reuse of expensive-to-create objects (such as database socket connections, thread workers, or socket handles) rather than repeatedly creating and destroying them.
- **Classification**: Creational & Concurrency Pattern.
- **Key Mechanism**:
  - A thread-safe queue holding available resources.
  - Client calls `acquire()` (blocks or raises timeout if exhausted).
  - Client returns resource with `release()` (or via a Python context manager).

## Architecture & Data Flow

```mermaid
sequenceDiagram
    participant Worker1 as Worker Thread 1
    participant Pool as ObjectPool (Capacity = 2)
    participant Worker2 as Worker Thread 2

    Worker1->>Pool: acquire()
    Pool-->>Worker1: DBConnection-1
    Worker2->>Pool: acquire()
    Pool-->>Worker2: DBConnection-2

    Note over Pool: Pool is now exhausted (0 available)
    Worker1->>Pool: release(DBConnection-1)
    Note over Pool: DBConnection-1 returned to queue
```

## FAANG Interview Significance
- How SQLAlchemy Connection Pooling (`QueuePool`), HikariCP (Java), and Gunicorn worker pools function under high load.
- Prevents database crashing from 50,000 simultaneous TCP handshakes.
