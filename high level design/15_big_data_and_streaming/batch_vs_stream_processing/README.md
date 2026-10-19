# Batch vs Stream Processing

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **Batch (Spark, MapReduce)**: High latency (hours), massive throughput, bounded datasets, perfect completeness.
- **Stream (Flink, Kafka Streams)**: Low latency (sub-second), unbounded event streams, sliding/tumbling windows.
