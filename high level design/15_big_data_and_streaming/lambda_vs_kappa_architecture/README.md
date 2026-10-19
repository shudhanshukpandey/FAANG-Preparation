# Lambda vs Kappa Architecture

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Lambda Architecture**: Dual layers (Speed Layer via Storm/Flink + Batch Layer via Hadoop) merged at the Serving Layer. Double maintenance burden.
- **Kappa Architecture**: Single stream-processing log (Kafka/Flink); reprocessing historical data is just replaying the log from offset 0.
