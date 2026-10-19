# CQRS (Command Query Responsibility Segregation)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Command Model**: Handles writes/mutations with domain validation and transactional integrity.
- **Query Model**: Optimized denormalized read views for lightning-fast UI rendering.
