# Feature Flags & Remote Configuration

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Decoupled Deployment from Release**: Code deployed dark in master; enabled via cloud config without re-deploying binaries.
- **Kill Switch**: Instantly disable misbehaving microservices or 3rd-party payment gateways.
