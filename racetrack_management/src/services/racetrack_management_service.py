from abc import ABC, abstractmethod


class IRaceTrackManagementService(ABC):

    @abstractmethod
    def create_booking(self, type_of_vehicle, vehicle_number, entry_time):
        ...

    @abstractmethod
    def extend_booking(self, vehicle_number, exit_time):
        ...

    @abstractmethod
    def get_revenue(self):
        ...
