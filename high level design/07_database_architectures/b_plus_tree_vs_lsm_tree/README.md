# Storage Engines: B+ Tree vs LSM-Tree

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

- **B+ Tree (Postgres, MySQL InnoDB)**: In-place page updates; optimized for high read throughput and range scans.
- **LSM-Tree (RocksDB, Cassandra, LevelDB)**: Append-only sequential writes to MemTable + WAL, periodically flushed to SSTables; optimized for massive write throughput.
