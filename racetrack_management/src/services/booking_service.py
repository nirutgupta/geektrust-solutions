from abc import ABC, abstractmethod
from typing import List

from src.models.booking import Booking


class IBookingService(ABC):

    @abstractmethod
    def create_booking(self, type_of_vehicle, vehicle_number, entry_time, exit_time, racetrack_id):
        pass

    @abstractmethod
    def extend_booking(self, vehicle_number, exit_time):
        pass

    @abstractmethod
    def get_all_bookings(self) -> List[Booking]:
        pass

    @abstractmethod
    def get_bookings_by_racetrack_id(self, racetrack_id):
        pass

    @abstractmethod
    def get_booking_by_vehicle_number(self, vehicle_number):
        pass
