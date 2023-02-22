from src.commands.racetrack_management_commands.racetrack_management_service_command import RaceTrackManagementServiceCommand


class ExtendBookingCommand(RaceTrackManagementServiceCommand):
    def execute(self, *args):
        self.rms.extend_booking(*args)
