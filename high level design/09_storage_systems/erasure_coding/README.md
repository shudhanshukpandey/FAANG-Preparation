# Erasure Coding Durability

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Replication vs Erasure Coding**: 3x replication has 200% storage overhead. Erasure coding (e.g. Reed-Solomon 8+4) provides equal durability with only 50% overhead.
- **Reconstruction**: Any $K$ out of $K+M$ fragments suffice to reconstruct the original data.
