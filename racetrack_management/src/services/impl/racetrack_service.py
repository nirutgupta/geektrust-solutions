from typing import List

from src.dao.racetrack_dao import RaceTrackDao
from src.models.racetrack.ractrack_impl import RaceTrack
from src.services.racetrack_service import IRaceTrackService


class RaceTrackService(IRaceTrackService):

    def __init__(self):
        self._dao = RaceTrackDao.get_instance()

    def add_racetrack(self):
        pass

    def get_racetrack_cost_per_hour(self, racetrack_id):
        racetrack = self._dao.get_racetrack_by_id(racetrack_id)
        return racetrack.cost_per_hour

    def get_racetrack_by_vehicle_type(self, racetrack_type):
        racetracks: List[RaceTrack] = self._dao.get_racetrack_by_vehicle_type(racetrack_type)
        racetracks.sort(key=lambda x: x.type.value)
        return racetracks

    def get_racetrack_by_id(self, racetrack_id) -> RaceTrack:
        return self._dao.get_racetrack_by_id(racetrack_id)

    def get_racetrack_type_by_id(self, racetrack_id):
        return self._dao.get_racetrack_by_id(racetrack_id).type
