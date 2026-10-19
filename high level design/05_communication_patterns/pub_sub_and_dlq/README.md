# Pub/Sub Broadcasting & Dead Letter Queues (DLQ)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **1-to-Many Fan-Out**: Multiple independent subscriber services consume from a single topic.
- **Dead Letter Queue**: Malformed messages that fail repeated processing are segregated to prevent queue blockage.
