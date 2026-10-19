"""Ride-Sharing & Cab Booking System (Mini-Uber).

Features:
- Driver and Rider profiles with coordinates.
- Spatial Proximity Search using Euclidean / Manhattan distance.
- Dynamic Surge Pricing Strategy based on demand-to-supply ratio.
- Trip Lifecycle State Machine (REQUESTED -> ACCEPTED -> IN_PROGRESS -> COMPLETED / CANCELLED).
- Rating and fare settlement.
"""

from __future__ import annotations

import math
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional


class TripStatus(Enum):
    REQUESTED = "REQUESTED"
    ACCEPTED = "ACCEPTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


@dataclass
class Location:
    x: float
    y: float

    def distance_to(self, other: Location) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


@dataclass
class Driver:
    driver_id: str
    name: str
    location: Location
    is_available: bool = True
    rating: float = 5.0
    total_ratings: int = 1


@dataclass
class Rider:
    rider_id: str
    name: str
    location: Location


@dataclass
class Trip:
    trip_id: str
    rider: Rider
    pickup: Location
    drop: Location
    driver: Optional[Driver] = None
    fare: float = 0.0
    status: TripStatus = TripStatus.REQUESTED


class SurgePricingStrategy:
    """Calculates surge multiplier based on demand and available supply."""
    def get_multiplier(self, demand: int, available_drivers: int) -> float:
        if available_drivers == 0:
            return 2.5
        ratio = demand / available_drivers
        if ratio > 2.0:
            return 2.0
        elif ratio > 1.2:
            return 1.4
        return 1.0


class CabBookingService:
    BASE_RATE_PER_KM = 12.0
    BASE_FARE = 30.0

    def __init__(self) -> None:
        self.drivers: Dict[str, Driver] = {}
        self.riders: Dict[str, Rider] = {}
        self.trips: Dict[str, Trip] = {}
        self.surge_strategy = SurgePricingStrategy()
        self._trip_counter = 0

    def register_driver(self, driver_id: str, name: str, location: Location) -> Driver:
        d = Driver(driver_id, name, location)
        self.drivers[driver_id] = d
        return d

    def register_rider(self, rider_id: str, name: str, location: Location) -> Rider:
        r = Rider(rider_id, name, location)
        self.riders[rider_id] = r
        return r

    def find_nearest_available_driver(self, pickup: Location, max_radius: float = 10.0) -> Optional[Driver]:
        best_driver = None
        min_dist = float("inf")

        for d in self.drivers.values():
            if d.is_available:
                dist = d.location.distance_to(pickup)
                if dist <= max_radius and dist < min_dist:
                    min_dist = dist
                    best_driver = d
        return best_driver

    def request_ride(self, rider_id: str, pickup: Location, drop: Location) -> Trip:
        rider = self.riders[rider_id]
        available_count = sum(1 for d in self.drivers.values() if d.is_available)
        demand_count = sum(1 for t in self.trips.values() if t.status == TripStatus.REQUESTED) + 1

        surge = self.surge_strategy.get_multiplier(demand_count, available_count)
        distance = pickup.distance_to(drop)
        fare = round((self.BASE_FARE + (distance * self.BASE_RATE_PER_KM)) * surge, 2)

        self._trip_counter += 1
        trip_id = f"TRIP_{self._trip_counter}"
        trip = Trip(trip_id=trip_id, rider=rider, pickup=pickup, drop=drop, fare=fare)

        driver = self.find_nearest_available_driver(pickup)
        if driver:
            trip.driver = driver
            trip.status = TripStatus.ACCEPTED
            driver.is_available = False

        self.trips[trip_id] = trip
        return trip

    def start_trip(self, trip_id: str) -> None:
        trip = self.trips[trip_id]
        if trip.status != TripStatus.ACCEPTED:
            raise ValueError(f"Cannot start trip with status {trip.status}")
        trip.status = TripStatus.IN_PROGRESS

    def complete_trip(self, trip_id: str, driver_rating: Optional[float] = None) -> None:
        trip = self.trips[trip_id]
        if trip.status != TripStatus.IN_PROGRESS:
            raise ValueError(f"Cannot complete trip with status {trip.status}")

        trip.status = TripStatus.COMPLETED
        if trip.driver:
            trip.driver.is_available = True
            trip.driver.location = trip.drop
            if driver_rating is not None:
                d = trip.driver
                d.rating = round(((d.rating * d.total_ratings) + driver_rating) / (d.total_ratings + 1), 2)
                d.total_ratings += 1

    def cancel_trip(self, trip_id: str) -> None:
        trip = self.trips[trip_id]
        if trip.status in (TripStatus.COMPLETED, TripStatus.CANCELLED):
            raise ValueError("Trip already finished")
        trip.status = TripStatus.CANCELLED
        if trip.driver:
            trip.driver.is_available = True


def run_tests() -> None:
    svc = CabBookingService()
    svc.register_driver("d1", "Bob", Location(1.0, 1.0))
    svc.register_driver("d2", "Charlie", Location(10.0, 10.0))
    svc.register_rider("r1", "Alice", Location(1.2, 1.2))

    trip = svc.request_ride("r1", Location(1.2, 1.2), Location(5.2, 5.2))
    assert trip.driver is not None
    assert trip.driver.driver_id == "d1"
    assert trip.status == TripStatus.ACCEPTED
    assert not trip.driver.is_available

    svc.start_trip(trip.trip_id)
    assert trip.status == TripStatus.IN_PROGRESS

    svc.complete_trip(trip.trip_id, driver_rating=5.0)
    assert trip.status == TripStatus.COMPLETED
    assert trip.driver.is_available is True
    assert trip.driver.location == Location(5.2, 5.2)

    print("✅ cab_booking_uber tests passed successfully!")


if __name__ == "__main__":
    run_tests()
