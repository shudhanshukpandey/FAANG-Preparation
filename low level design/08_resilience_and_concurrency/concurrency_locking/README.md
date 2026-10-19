# Concurrency & Locking: Optimistic vs. Pessimistic

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.


## Overview
- **Intent**: Manage concurrent data access and prevent race conditions (e.g. double spending, inventory overselling, or lost updates).
- **Two Dominant Philosophies**:
  1. **Pessimistic Locking**:
     - *"Conflicts will happen often, so lock the row exclusively."*
     - In SQL: `SELECT * FROM seats WHERE id = 42 FOR UPDATE;`
     - In Python: `threading.Lock` / Mutex.
     - Pro: Guarantees 0 write conflicts.
     - Con: Potential deadlocks, high latency under heavy contention.
  2. **Optimistic Locking**:
     - *"Conflicts are rare, so don't lock; check for conflicts at write time using a version number."*
     - In SQL: `UPDATE products SET stock = stock - 1, version = version + 1 WHERE id = 10 AND version = 5;`
     - If rows updated == 0, another transaction won the race; retry or abort.
     - Pro: High read throughput, zero database locks.
     - Con: High retry overhead during flash sales.

## Architecture & Data Flow

```mermaid
sequenceDiagram
    participant UserA as User A (Thread 1)
    participant DB as Product Table (stock=1, version=1)
    participant UserB as User B (Thread 2)

    UserA->>DB: Read product (stock=1, version=1)
    UserB->>DB: Read product (stock=1, version=1)

    Note over UserA,DB: User A submits first
    UserA->>DB: UPDATE WHERE version=1 -> version=2
    DB-->>UserA: SUCCESS (1 row updated)

    Note over UserB,DB: User B submits with stale version=1
    UserB->>DB: UPDATE WHERE version=1 -> version=2
    DB-->>UserB: FAILED (0 rows updated! Concurrency Conflict!)
    Note over UserB: Abort or Retry with new version
```

## FAANG Interview Significance
- Essential for: Concert ticket booking (BookMyShow / Ticketmaster), Flash Sale inventory (Amazon Big Billion Days), and Banking transfers.
