from src.commands.command import ICommand
from src.services.impl.racetrack_management_service import RaceTrackManagementService
from src.services.racetrack_management_service import IRaceTrackManagementService


class RaceTrackManagementServiceCommand(ICommand):
    def __init__(self):
        self.rms: IRaceTrackManagementService = RaceTrackManagementService()

    def execute(self):
        raise NotImplemented
