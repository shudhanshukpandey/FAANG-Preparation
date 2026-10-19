# Distributed Tracing & RED Metrics

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Tracing (Jaeger, Zipkin, OpenTelemetry)**: Propagates `traceparent` HTTP headers across microservices to isolate bottleneck spans.
- **RED Metrics**: Rate (requests/sec), Errors (failures/sec), Duration (p95/p99 latency distribution).
