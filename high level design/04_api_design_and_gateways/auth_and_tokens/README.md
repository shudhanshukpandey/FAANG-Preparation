# Stateless JWT & Token Authentication

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Header.Payload.Signature**: Self-contained cryptographic proof of identity.
- **Stateless Verification**: Microservices verify signatures locally using public key / secret without database lookups.
