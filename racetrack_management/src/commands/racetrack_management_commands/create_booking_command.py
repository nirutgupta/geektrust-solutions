from src.commands.racetrack_management_commands.racetrack_management_service_command import RaceTrackManagementServiceCommand


class CreateBookingCommand(RaceTrackManagementServiceCommand):
    def execute(self, *args):
        self.rms.create_booking(*args)
