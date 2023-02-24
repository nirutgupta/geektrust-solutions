from collections import defaultdict

from src.models.booking import Booking
from src.services.meeting_room import MeetingRoomService


class BookingService:

    def __init__(self):
        self.bookings = defaultdict(list)
        self.meeting_room_svc = MeetingRoomService()

    def get_bookings(self, meeting_room_name):
        pass

    def create_booking(self, meeting_room_name, time_range, person_capacity):
        self.bookings[meeting_room_name].append(Booking(time_range, person_capacity, meeting_room_name))
