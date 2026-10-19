# Database Connection Pooling

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Connection Overhead**: TLS handshake and PostgreSQL backend process spawning cost 20-50ms per query.
- **Connection Pooling (PgBouncer, HikariCP)**: Maintains warm open socket pool, multiplexing thousands of application threads into a controlled pool.
