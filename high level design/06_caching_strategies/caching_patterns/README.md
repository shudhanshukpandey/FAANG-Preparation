# Caching Patterns: Cache-Aside vs Write-Through vs Write-Behind

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Cache-Aside (Lazy Loading)**: Application reads cache; on miss, reads DB and populates cache.
- **Write-Through**: Application writes to cache; cache synchronously writes to DB.
- **Write-Behind (Write-Back)**: Application writes to cache; cache asynchronously batches writes to DB.
