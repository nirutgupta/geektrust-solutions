from src.models.booking import Booking


class BookingDao:
    __instance = None

    def __init__(self):
        self._vehicle_number_to_booking = {}
        self.__init_db()

    def __init_db(self):
        pass

    @classmethod
    def get_instance(cls):
        if BookingDao.__instance is None:
            cls.__instance = BookingDao()
        return cls.__instance

    def add_booking(self, booking: Booking):
        self._vehicle_number_to_booking[booking.vehicle_number] = booking

    def get_booking_by_vehicle_number(self, vehicle_number):
        return self._vehicle_number_to_booking[vehicle_number]

    def get_all_bookings(self):
        return self._vehicle_number_to_booking.values()
