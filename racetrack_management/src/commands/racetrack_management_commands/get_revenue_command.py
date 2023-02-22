from src.commands.racetrack_management_commands.racetrack_management_service_command import RaceTrackManagementServiceCommand


class RevenueCommand(RaceTrackManagementServiceCommand):
    def execute(self, *args):
        self.rms.get_revenue()
