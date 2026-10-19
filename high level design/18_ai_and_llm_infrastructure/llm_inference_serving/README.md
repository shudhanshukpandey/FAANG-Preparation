# LLM Inference Serving: Continuous Batching & PagedAttention

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Prefill vs Decode**: Prefill is compute-bound (processes entire prompt matrix in parallel); Decode is memory-bandwidth bound (generates one autoregressive token at a time).
- **Continuous Batching (vLLM, TGI)**: New requests join the batch at each token iteration rather than waiting for preceding requests to finish.
- **PagedAttention**: Virtual memory paging eliminates KV-cache fragmentation on GPU HBM.
