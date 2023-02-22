from dataclasses import dataclass

from src.models.passenger_type import PassengerType


@dataclass
class Trip:
    source: str
    passenger_type: PassengerType
    return_trip: bool = False
