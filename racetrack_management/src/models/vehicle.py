from dataclasses import dataclass
from src.enums.vehicle_type import VehicleType


@dataclass
class Vehicle:
    number: str
    type: VehicleType
