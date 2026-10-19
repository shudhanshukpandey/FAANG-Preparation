# Backend for Frontend (BFF) & Sidecar Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Backend for Frontend (BFF)**: Custom API gateway tailored for specific UI form factors (iOS vs Desktop vs SmartTV).
- **Sidecar Proxy (Envoy / Istio)**: Sits alongside application container, handling mTLS, distributed tracing, and metrics transparently.
