# Two-Phase Commit (2PC)

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Phase 1 (Prepare)**: Coordinator asks all participants to vote YES/NO and write undo/redo logs.
- **Phase 2 (Commit/Abort)**: If all vote YES, commit; otherwise abort.
- **Flaw**: Blocking coordinator failure blocks participants holding table locks indefinitely.
