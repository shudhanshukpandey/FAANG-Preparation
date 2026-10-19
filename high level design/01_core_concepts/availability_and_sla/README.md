# High Availability, SLAs, and Redundancy Math

> [!TIP]
> **Interactive Diagram**: Open [diagram.html](diagram.html) in your browser to explore the interactive animated data flow with theme toggles and SVG/image export.

## The Availability "Nines" Table

| Availability | Downtime per Year | Downtime per Month | Downtime per Day |
| :--- | :--- | :--- | :--- |
| **99% (Two 9s)** | 3.65 days | 7.31 hours | 14.4 minutes |
| **99.9% (Three 9s)** | 8.77 hours | 43.8 minutes | 1.44 minutes |
| **99.99% (Four 9s)** | 52.6 minutes | 4.38 minutes | 8.64 seconds |
| **99.999% (Five 9s)** | 5.26 minutes | 26.3 seconds | 864 milliseconds |

## System Reliability Math
1. **Serial Components**:
   $$A_{\text{system}} = A_1 \times A_2 \times \dots \times A_n$$
   *Adding serial dependencies strictly reduces overall availability.*
2. **Parallel (Redundant) Components**:
   $$A_{\text{system}} = 1 - (1 - A_1) \times (1 - A_2) \times \dots \times (1 - A_n)$$
   *Adding independent redundant failover paths exponentially increases availability.*
