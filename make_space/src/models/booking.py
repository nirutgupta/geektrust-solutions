from dataclasses import dataclass

from src.models.event import Event


@dataclass
class Booking:
    time_range: Event
    no_of_persons: int
    meeting_room_name: str
