from src.enums.vehicle_type import VehicleType
from src.models.vehicle import Vehicle


class Booking:
    def __init__(self, vehicle, entry_time, exit_time, racetrack_id):
        self._vehicle: Vehicle = vehicle
        self._entry_time = entry_time
        self._init_exit_time = exit_time
        self._exit_time = exit_time
        self._racetrack_id = racetrack_id
        self._booking_id = self.vehicle_number

    def set_exit_time(self, value):
        self._exit_time = value

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def entry_time(self):
        return self._entry_time

    @property
    def exit_time(self):
        return self._exit_time

    @property
    def racetrack_id(self):
        return self._racetrack_id

    @property
    def vehicle_number(self):
        return self._vehicle.number

    @property
    def id(self):
        return self._booking_id

    @property
    def is_extended(self):
        if self._init_exit_time < self._exit_time:
            return True
        return False

    def get_extended_by_in_seconds(self) -> int:
        return (self._exit_time-self._init_exit_time).seconds
