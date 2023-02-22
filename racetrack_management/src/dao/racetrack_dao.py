from src.models.racetrack.ractrack_impl import RaceTrack
from src.enums.racetrack_type import RaceTrackType
from src.enums.vehicle_type import VehicleType


class RaceTrackDao:
    __instance = None

    def __init__(self):
        self._racetrack_id_to_racetrack = {}
        self.__init_db()

    def __init_db(self):
        self.add_racetrack(RaceTrack(RaceTrackType.REGULAR, VehicleType.BIKE, 4, 60))
        self.add_racetrack(RaceTrack(RaceTrackType.REGULAR, VehicleType.CAR, 2, 120))
        self.add_racetrack(RaceTrack(RaceTrackType.REGULAR, VehicleType.SUV, 2, 200))
        self.add_racetrack(RaceTrack(RaceTrackType.VIP, VehicleType.CAR, 1, 250))
        self.add_racetrack(RaceTrack(RaceTrackType.VIP, VehicleType.SUV, 1, 300))

    @classmethod
    def get_instance(cls):
        if RaceTrackDao.__instance is None:
            cls.__instance = RaceTrackDao()
        return cls.__instance

    def add_racetrack(self, racetrack):
        self._racetrack_id_to_racetrack[racetrack.id] = racetrack

    def get_racetrack_by_id(self, id):
        return self._racetrack_id_to_racetrack[id]

    def get_racetrack_by_vehicle_type(self, vehicle_type) -> list:
        res = []
        for racetrack in self._racetrack_id_to_racetrack.values():
            if racetrack.vehicle_type == vehicle_type:
                res.append(racetrack)
        return res
