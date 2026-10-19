# Vector Database Internals: HNSW & Quantization

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **HNSW (Hierarchical Navigable Small World)**: Multi-layer graph index mimicking skip lists; coarse top layers jump long distances, fine bottom layer refines local clusters.
- **Product Quantization (PQ)**: Compresses 1536-dimensional floating point vectors by 95% into short byte codes.
