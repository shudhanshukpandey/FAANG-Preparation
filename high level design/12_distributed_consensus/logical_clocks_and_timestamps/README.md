# Logical Clocks & Vector Clocks

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Lamport Clocks**: Monotonically increasing integers capturing causal order ($a \to b$).
- **Vector Clocks**: Array of counters tracking per-node causal history, detecting concurrent conflicting updates.
