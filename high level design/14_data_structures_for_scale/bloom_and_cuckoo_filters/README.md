# Bloom & Cuckoo Filters

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Space Efficiency**: Millions of items tracked in megabytes of RAM.
- **Guarantees**: Zero False Negatives (if Bloom says NO, item definitely doesn't exist); Low False Positives (if YES, verify in disk/DB).
