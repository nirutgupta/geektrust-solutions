from src.dao.booking_dao import BookingDao
from src.models.booking import Booking
from src.models.vehicle import Vehicle
from src.services.booking_service import IBookingService


class BookingService(IBookingService):

    def __init__(self):
        self._dao = BookingDao.get_instance()

    def create_booking(self, type_of_vehicle, vehicle_number, entry_time, exit_time, racetrack_id):
        booking = Booking(Vehicle(vehicle_number, type_of_vehicle), entry_time, exit_time, racetrack_id)
        self._dao.add_booking(booking)
        return booking.id

    def extend_booking(self, vehicle_number, exit_time):
        booking = self._dao.get_booking_by_vehicle_number(vehicle_number)
        booking.set_exit_time(exit_time)

    def get_all_bookings(self):
        return self._dao.get_all_bookings()

    def get_bookings_by_racetrack_id(self, racetrack_id):
        res = []
        for booking in self.get_all_bookings():
            if booking.racetrack_id == racetrack_id:
                res.append(booking)
        return res

    def get_booking_by_vehicle_number(self, vehicle_number):
        return self._dao.get_booking_by_vehicle_number(vehicle_number)
