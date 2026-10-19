# Cache Stampede & Proactive Warming

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Cache Stampede (Thundering Herd)**: When a popular key expires, thousands of concurrent requests miss simultaneously and overwhelm the database.
- **Solutions**:
  1. **Mutex Lock on Miss**: Only 1 request queries DB; others wait for cache to populate.
  2. **XFetch (Probabilistic Early Refresh)**: Background worker refreshes key before it expires based on compute time and time left.
  3. **Cache Warming**: Pre-populating expected keys prior to scheduled marketing spikes.
