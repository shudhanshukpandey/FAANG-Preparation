# Latency, Throughput, Bandwidth & Little's Law

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## Fundamental Definitions
- **Latency**: Time taken for a single unit of data to travel from origin to destination (measured in milliseconds).
- **Throughput**: Number of actions or requests executed per unit time (e.g. Requests Per Second, QPS).
- **Bandwidth**: Maximum data transfer capacity of a physical or logical channel (e.g. 10 Gbps).

## Little's Law
$$L = \lambda \times W$$
- $L$ = Average number of requests in the system (Concurrency / In-Flight requests).
- $\lambda$ = Arrival rate / Throughput (Requests per second).
- $W$ = Average time a request spends in the system (Average Latency).

*Example*: If your API handles **5,000 QPS** with an average latency of **200 ms (0.2s)**, your backend thread pool must sustain:
$$L = 5,000 \times 0.2 = 1,000 \text{ concurrent in-flight requests}.$$
