"""Parking Lot System: Production-grade implementation using Strategy and Factory patterns."""

from abc import ABC, abstractmethod
from enum import Enum
import time
import uuid
from typing import Dict, List, Optional


# 1. Enums
class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3


class SpotType(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


# 2. Vehicle Hierarchy
class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType) -> None:
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate, VehicleType.MOTORCYCLE)


class Car(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate, VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate, VehicleType.TRUCK)


# 3. Parking Spot
class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType) -> None:
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.parked_vehicle: Optional[Vehicle] = None

    @property
    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        if self.spot_type == SpotType.MOTORCYCLE:
            return vehicle.vehicle_type == VehicleType.MOTORCYCLE
        elif self.spot_type == SpotType.COMPACT:
            return vehicle.vehicle_type in (VehicleType.MOTORCYCLE, VehicleType.CAR)
        elif self.spot_type == SpotType.LARGE:
            return True
        return False

    def park(self, vehicle: Vehicle) -> None:
        if not self.is_available:
            raise RuntimeError(f"Spot {self.spot_id} is already occupied.")
        self.parked_vehicle = vehicle

    def vacate(self) -> None:
        self.parked_vehicle = None


# 4. Ticket
class Ticket:
    def __init__(self, spot_id: str, license_plate: str, vehicle_type: VehicleType) -> None:
        self.ticket_id = f"TKT-{str(uuid.uuid4())[:8].upper()}"
        self.spot_id = spot_id
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.entry_time = time.time()


# 5. Fee Calculation Strategy Pattern
class FeeCalculationStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, duration_hours: float, vehicle_type: VehicleType) -> float:
        pass


class FlatRatePerHourStrategy(FeeCalculationStrategy):
    RATES = {
        VehicleType.MOTORCYCLE: 10.0,
        VehicleType.CAR: 20.0,
        VehicleType.TRUCK: 50.0,
    }

    def calculate_fee(self, duration_hours: float, vehicle_type: VehicleType) -> float:
        rate = self.RATES[vehicle_type]
        # Minimum 1 hour charge
        hours = max(1.0, duration_hours)
        return round(hours * rate, 2)


# 6. Parking Lot Controller
class ParkingLot:
    def __init__(self, name: str, fee_strategy: FeeCalculationStrategy) -> None:
        self.name = name
        self.fee_strategy = fee_strategy
        self.spots: Dict[str, ParkingSpot] = {}
        self.active_tickets: Dict[str, Ticket] = {}

    def add_spot(self, spot: ParkingSpot) -> None:
        self.spots[spot.spot_id] = spot

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        # Allocation strategy: Find first available spot that fits vehicle
        for spot in self.spots.values():
            if spot.is_available and spot.can_fit_vehicle(vehicle):
                spot.park(vehicle)
                ticket = Ticket(spot.spot_id, vehicle.license_plate, vehicle.vehicle_type)
                self.active_tickets[ticket.ticket_id] = ticket
                print(f"[ParkingLot] Vehicle {vehicle.license_plate} parked in Spot {spot.spot_id} (Issued Ticket {ticket.ticket_id}).")
                return ticket
        raise RuntimeError(f"No available spot found for vehicle {vehicle.license_plate}!")

    def unpark_vehicle(self, ticket_id: str, simulated_hours_parked: float = 2.5) -> float:
        if ticket_id not in self.active_tickets:
            raise KeyError(f"Invalid ticket ID: {ticket_id}")

        ticket = self.active_tickets.pop(ticket_id)
        spot = self.spots[ticket.spot_id]
        spot.vacate()

        fee = self.fee_strategy.calculate_fee(simulated_hours_parked, ticket.vehicle_type)
        print(f"[ParkingLot] Vehicle {ticket.license_plate} exited from Spot {spot.spot_id}. Parked {simulated_hours_parked} hrs. Total Fee: ${fee:.2f}")
        return fee


if __name__ == "__main__":
    lot = ParkingLot("Downtown Prime Garage", FlatRatePerHourStrategy())

    # Add spots
    lot.add_spot(ParkingSpot("M-1", SpotType.MOTORCYCLE))
    lot.add_spot(ParkingSpot("C-1", SpotType.COMPACT))
    lot.add_spot(ParkingSpot("L-1", SpotType.LARGE))

    # Vehicles arrive
    bike = Motorcycle("KA-01-BK-999")
    car = Car("MH-02-CR-1234")
    truck = Truck("DL-01-TK-5555")

    # Park vehicles
    t1 = lot.park_vehicle(bike)
    t2 = lot.park_vehicle(car)
    t3 = lot.park_vehicle(truck)

    # Vehicles exit
    print("\n--- Processing Exits ---")
    lot.unpark_vehicle(t1.ticket_id, simulated_hours_parked=1.5)
    lot.unpark_vehicle(t2.ticket_id, simulated_hours_parked=3.0)
