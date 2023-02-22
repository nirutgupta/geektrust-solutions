from abc import ABC, abstractmethod


class IRaceTrackService(ABC):

    @abstractmethod
    def add_racetrack(self):
        pass

    @abstractmethod
    def get_racetrack_by_vehicle_type(self, racetrack_type):
        pass

    @abstractmethod
    def get_racetrack_cost_per_hour(self, racetrack_id):
        pass

    @abstractmethod
    def get_racetrack_by_id(self, racetrack_id):
        pass

    @abstractmethod
    def get_racetrack_type_by_id(self, racetrack_id):
        pass

