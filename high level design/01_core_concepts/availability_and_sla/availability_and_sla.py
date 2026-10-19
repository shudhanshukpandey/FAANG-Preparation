"""High Availability & SLA Math Simulation.

Demonstrates:
- SLA calculation: Downtime budgets for 99.9% (Three 9s) vs 99.999% (Five 9s).
- Redundancy Math: Serial vs Parallel component availability.
- MTBF (Mean Time Between Failures) and MTTR (Mean Time To Repair).
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SLACalculator:
    availability_percentage: float

    def annual_downtime_minutes(self) -> float:
        total_minutes = 365.25 * 24 * 60
        downtime_ratio = (100.0 - self.availability_percentage) / 100.0
        return round(total_minutes * downtime_ratio, 2)

    @staticmethod
    def composite_serial_availability(availabilities: list[float]) -> float:
        """Serial system availability = A1 * A2 * ... * An"""
        total = 1.0
        for a in availabilities:
            total *= a
        return round(total, 5)

    @staticmethod
    def composite_parallel_availability(availabilities: list[float]) -> float:
        """Parallel system availability = 1 - (1 - A1) * (1 - A2) ..."""
        unavailability = 1.0
        for a in availabilities:
            unavailability *= (1.0 - a)
        return round(1.0 - unavailability, 5)


def run_tests() -> None:
    sla_3_nines = SLACalculator(99.9)
    sla_5_nines = SLACalculator(99.999)

    # 3 nines allows ~526 minutes (8.7 hours) downtime per year
    assert 525.0 <= sla_3_nines.annual_downtime_minutes() <= 527.0
    # 5 nines allows ~5.26 minutes downtime per year
    assert 5.0 <= sla_5_nines.annual_downtime_minutes() <= 5.5

    # Serial: 99% * 99% = 98.01%
    assert SLACalculator.composite_serial_availability([0.99, 0.99]) == 0.98010
    # Parallel (active-active): 1 - (0.01 * 0.01) = 99.99%
    assert SLACalculator.composite_parallel_availability([0.99, 0.99]) == 0.99990
    print("✅ availability_and_sla tests passed!")


if __name__ == "__main__":
    run_tests()
