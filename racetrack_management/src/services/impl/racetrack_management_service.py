import math

from typing import List
from datetime import timedelta

from src.models.racetrack.racetrack import IRaceTrack
from src.enums.vehicle_type import VehicleType
from src.enums.racetrack_type import RaceTrackType
from src.services.booking_service import IBookingService
from src.services.impl.booking_service import BookingService
from src.services.impl.racetrack_service import RaceTrackService
from src.services.racetrack_management_service import IRaceTrackManagementService
from src.services.racetrack_service import IRaceTrackService
from src.utils.exceptions import RaceTrackFullException
from src.utils.helpers import get_datetime, convert_seconds_to_minutes, convert_seconds_to_hours
from src.utils.constants import RACETRACK_ENTRY_TIME, RACETRACK_EXIT_TIME, \
    MINIMUM_BOOKING_TIME_IN_HOURS, FREE_EXTENDED_BOOKING_TIME_IN_MINUTES, EXTENDED_BOOKING_COST_PER_HOUR


class RaceTrackManagementService(IRaceTrackManagementService):

    def __init__(self):
        self._racetrack_service: IRaceTrackService = RaceTrackService()
        self._booking_service: IBookingService = BookingService()

    def __find_racetrack(self, type_of_vehicle, entry_time, exit_time):
        racetracks: List[IRaceTrack] = self._racetrack_service.get_racetrack_by_vehicle_type(type_of_vehicle)
        for racetrack in racetracks:
            bookings = self._booking_service.get_bookings_by_racetrack_id(racetrack.id)
            if self.__is_racetrack_available_for_booking(bookings, entry_time, exit_time, racetrack.no_of_vehicles):
                return racetrack.id
        raise RaceTrackFullException()

    @staticmethod
    def __is_racetrack_available_for_booking(bookings, entry_time, exit_time, number_of_vehicles) -> bool:
        count = 1
        for booking in bookings:
            if booking.entry_time < entry_time < booking.exit_time or booking.entry_time < exit_time < booking.exit_time:
                count += 1
        return True if count <= number_of_vehicles else False

    @staticmethod
    def __is_racetrack_available_for_booking_extension(bookings, vehicle_number, exit_time,
                                                       number_of_vehicles) -> bool:
        count = 1
        for booking in bookings:
            if booking.vehicle_number == vehicle_number:
                continue
            if booking.entry_time < exit_time < booking.exit_time:
                count += 1
        return True if count <= number_of_vehicles else False

    def create_booking(self, type_of_vehicle, vehicle_number, entry_time):
        entry_time = get_datetime(entry_time)
        exit_time = entry_time + timedelta(hours=MINIMUM_BOOKING_TIME_IN_HOURS)
        type_of_vehicle = getattr(VehicleType, type_of_vehicle)
        if entry_time < get_datetime(RACETRACK_ENTRY_TIME) or exit_time > get_datetime(RACETRACK_EXIT_TIME):
            print("INVALID_ENTRY_TIME")
            return
        try:
            racetrack_id = self.__find_racetrack(type_of_vehicle, entry_time, exit_time)
        except RaceTrackFullException:
            print("RACETRACK_FULL")
            return
        self._booking_service.create_booking(type_of_vehicle, vehicle_number, entry_time, exit_time, racetrack_id)
        print("SUCCESS")

    def extend_booking(self, vehicle_number, exit_time):
        exit_time = get_datetime(exit_time)
        if exit_time > get_datetime(RACETRACK_EXIT_TIME):
            print("INVALID EXIT TIME")
            return
        booking = self._booking_service.get_booking_by_vehicle_number(vehicle_number)
        bookings = self._booking_service.get_bookings_by_racetrack_id(booking.racetrack_id)
        racetrack = self._racetrack_service.get_racetrack_by_id(booking.racetrack_id)
        if not self.__is_racetrack_available_for_booking_extension(bookings, vehicle_number, exit_time,
                                                                   racetrack.no_of_vehicles):
            print("RACETRACK_FULL")
            return
        self._booking_service.extend_booking(vehicle_number, exit_time)
        print("SUCCESS")

    def get_revenue(self):
        bookings = self._booking_service.get_all_bookings()
        revenue_earned_by_regular_racetrack = 0
        revenue_earned_by_vip_racetrack = 0
        for booking in bookings:
            cost_per_hour = self._racetrack_service.get_racetrack_cost_per_hour(booking.racetrack_id)
            booking_cost = (cost_per_hour * MINIMUM_BOOKING_TIME_IN_HOURS)
            if booking.is_extended:
                extended_booking_time_in_seconds = booking.get_extended_by_in_seconds()
                if convert_seconds_to_minutes(extended_booking_time_in_seconds) >= FREE_EXTENDED_BOOKING_TIME_IN_MINUTES:
                    hours = math.ceil(convert_seconds_to_hours(extended_booking_time_in_seconds))
                    extended_booking_fee = hours * EXTENDED_BOOKING_COST_PER_HOUR
                    booking_cost += extended_booking_fee
            racetrack_type = self._racetrack_service.get_racetrack_type_by_id(booking.racetrack_id)
            if racetrack_type == RaceTrackType.VIP:
                revenue_earned_by_vip_racetrack += booking_cost
            else:
                revenue_earned_by_regular_racetrack += booking_cost
        print(f"{revenue_earned_by_regular_racetrack}\t{revenue_earned_by_vip_racetrack}")
