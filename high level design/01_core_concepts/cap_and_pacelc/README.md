# CAP & PACELC Theorem

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## The CAP Theorem
In an asynchronous network with unavoidable partitions ($P$):
- **Consistency ($CP$)**: Every read receives the most recent write or an error. (e.g. Etcd, ZooKeeper, CockroachDB).
- **Availability ($AP$)**: Every non-failing node returns a response, without guaranteeing it contains the most recent write. (e.g. Cassandra, DynamoDB, CouchDB).

## The PACELC Theorem
CAP only addresses behavior during a network partition ($P$). PACELC extends this to normal operating conditions:
$$\text{If } \mathbf{P} \rightarrow (\mathbf{A} \lor \mathbf{C}); \quad \mathbf{E} \text{ (Else)} \rightarrow (\mathbf{L} \lor \mathbf{C})$$
- **PC/EC** (e.g. Spanner, CockroachDB): Consistent both during partition and normal operation.
- **PA/EL** (e.g. DynamoDB, Cassandra, Riak): Available during partition; minimizes Latency over Consistency normally.
