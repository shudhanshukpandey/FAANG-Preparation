# Event Sourcing Architecture

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Append-Only Log**: Instead of mutating database rows in-place, every state transition is recorded as an immutable business event.
- **Audit & Time-Travel**: Current state is derived by replaying the event log up to any given point in time.
