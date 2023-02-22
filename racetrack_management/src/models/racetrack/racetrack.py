
from abc import ABC, abstractmethod


class IRaceTrack(ABC):
    start = "1PM"
    end = "8PM"
    __id = 0

    @classmethod
    def _generate_id(cls):
        cls.__id += 1
        return cls.__id

    @property
    @abstractmethod
    def type(self):
        pass

    @property
    @abstractmethod
    def no_of_vehicles(self):
        pass

    @property
    @abstractmethod
    def cost_per_hour(self):
        pass

    @property
    @abstractmethod
    def racetrack_type(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass
