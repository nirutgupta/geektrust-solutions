from src.commands.racetrack_management_commands.create_booking_command import CreateBookingCommand
from src.commands.racetrack_management_commands.extend_booking_command import ExtendBookingCommand
from src.commands.racetrack_management_commands.get_revenue_command import RevenueCommand


class RaceTrackManagementCommandFactory:

    @staticmethod
    def get_instance(command_str):
        if command_str == "BOOK":
            return CreateBookingCommand()
        elif command_str == "ADDITIONAL":
            return ExtendBookingCommand()
        else:
            return RevenueCommand()
