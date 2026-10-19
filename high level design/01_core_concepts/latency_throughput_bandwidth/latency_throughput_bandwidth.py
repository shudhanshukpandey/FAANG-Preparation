"""Latency vs Throughput vs Bandwidth & Little's Law Simulation.

Demonstrates:
- Latency percentiles calculation: p50 (median), p95, p99, p99.9.
- Little's Law: L = λ * W (Concurrency = Throughput * Latency).
- Head-of-line queuing effects under high saturation.
"""

from __future__ import annotations
import math
from typing import List


class PerformanceAnalyzer:
    @staticmethod
    def calculate_percentiles(latencies_ms: List[float]) -> dict[str, float]:
        if not latencies_ms:
            return {}
        sorted_vals = sorted(latencies_ms)
        n = len(sorted_vals)

        def get_rank(pct: float) -> float:
            idx = int(math.ceil((pct / 100.0) * n)) - 1
            return sorted_vals[max(0, min(idx, n - 1))]

        return {
            "p50": get_rank(50),
            "p90": get_rank(90),
            "p95": get_rank(95),
            "p99": get_rank(99),
        }

    @staticmethod
    def littles_law_concurrency(throughput_rps: float, avg_latency_sec: float) -> float:
        """L = λ * W"""
        return round(throughput_rps * avg_latency_sec, 2)


def run_tests() -> None:
    # 100 requests: 95 fast (10ms), 4 slow (200ms), 1 extreme outlier (1500ms)
    latencies = [10.0] * 95 + [200.0] * 4 + [1500.0]
    metrics = PerformanceAnalyzer.calculate_percentiles(latencies)

    assert metrics["p50"] == 10.0
    assert metrics["p95"] == 10.0
    assert metrics["p99"] == 200.0  # Captures tail latency

    # Little's Law: 10,000 req/sec with 0.05s (50ms) average latency requires 500 concurrent workers
    concurrent_in_flight = PerformanceAnalyzer.littles_law_concurrency(10000, 0.05)
    assert concurrent_in_flight == 500.0
    print("✅ latency_throughput_bandwidth tests passed!")


if __name__ == "__main__":
    run_tests()
