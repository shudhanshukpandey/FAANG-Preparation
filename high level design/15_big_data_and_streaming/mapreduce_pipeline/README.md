# MapReduce Distributed Pipeline

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Map Phase**: Transforms input records into intermediate key-value pairs.
- **Shuffle & Sort**: Hashes keys to partition intermediate data to identical reducer workers.
- **Reduce Phase**: Aggregates grouped keys into output files.
