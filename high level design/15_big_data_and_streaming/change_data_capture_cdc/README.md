# Change Data Capture (CDC) & The Outbox Pattern

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **WAL Tailing (Debezium)**: Reads database write-ahead log directly, converting row changes into Kafka streaming events.
- **Transactional Outbox**: Writes application event in the same atomic SQL transaction as business entities.
