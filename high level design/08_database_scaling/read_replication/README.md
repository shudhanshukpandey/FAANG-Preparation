# Primary-Replica Read Scaling & Replication Lag

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Write Path**: Direct to Primary instance.
- **Read Path**: Scaled horizontally across multiple read replicas.
- **Replication Lag**: Time delta between primary WAL commit and replica execution. Requires sticky routing or read-after-write headers for recently updated users.
