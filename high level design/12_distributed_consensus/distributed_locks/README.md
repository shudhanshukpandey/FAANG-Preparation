# Distributed Locks & Fencing Tokens

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Lease Time-to-Live (TTL)**: Automatic release prevents deadlocks during worker death.
- **Fencing Tokens**: Monotonically increasing numbers sent to storage to reject delayed writes from GC-paused workers (Martin Kleppmann Redis Redlock critique).
