from src.models.racetrack.racetrack import IRaceTrack


class RaceTrack(IRaceTrack):
    def __init__(self, racetrack_type, vehicle_type, no_of_vehicles, cost_per_hour):
        self._racetrack_type = racetrack_type
        self._vehicle_type = vehicle_type
        self._no_of_vehicles = no_of_vehicles
        self._cost_per_hour = cost_per_hour
        self._id = self._generate_id()

    @property
    def type(self):
        return self._racetrack_type

    @property
    def no_of_vehicles(self):
        return self._no_of_vehicles

    @property
    def cost_per_hour(self):
        return self._cost_per_hour

    @property
    def racetrack_type(self):
        return self._racetrack_type

    @property
    def id(self):
        return self._id

    @property
    def vehicle_type(self):
        return self._vehicle_type
