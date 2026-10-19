# Bulkhead Pattern & Strangler Fig Migration

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Bulkhead Pattern**: Partitions resource pools (thread pools, connection slots) so a failure in a secondary service cannot exhaust resources for critical services.
- **Strangler Fig Pattern**: Gradually replaces legacy monolith endpoints by routing traffic to new microservices one route at a time.
