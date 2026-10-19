# Deployment Strategies: Blue-Green & Canary

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Blue-Green**: Two identical production environments; router flips 100% traffic instantly. Fast rollback, high idle cost.
- **Canary Deployment**: Routes 1%-5% of real user traffic to new version; monitors error rates before full rollout.
