# Health Checking & Failover

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Active Probes**: HTTP/TCP/gRPC health checks executed periodically.
- **Flapping Prevention**: Hysteresis requires multiple consecutive failures to eject, and multiple consecutive successes to recover.
