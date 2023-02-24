from src.exceptions import NoVacantRoomException, IncorrectTimeRangeException, IncorrectTimeException
from src.models.event import Event
from src.services.booking import BookingService
from src.services.meeting_room import MeetingRoomService


class MakeSpaceService:

    def __init__(self):
        self.__booking_service = BookingService()
        self.__meeting_room_service = MeetingRoomService()

    def create_booking(self, start_time, end_time, person_capacity):
        person_capacity = int(person_capacity)
        try:
            time_range = self.__get_time_range(start_time, end_time)
            meeting_room = self.__meeting_room_service.get_meeting_room(time_range, person_capacity)
        except (IncorrectTimeRangeException, IncorrectTimeException):
            print("INCORRECT_INPUT")
            return
        except NoVacantRoomException:
            print("NO_VACANT_ROOM")
            return

        self.__booking_service.create_booking(meeting_room.get_meeting_room_name(), time_range, person_capacity)
        self.__meeting_room_service.create_event(meeting_room, time_range)
        print(meeting_room.get_meeting_room_name())

    def get_available_rooms(self, start_time, end_time):
        try:
            time_range = self.__get_time_range(start_time, end_time)
            available_rooms = self.__meeting_room_service.get_meeting_rooms(time_range)
        except (IncorrectTimeRangeException, IncorrectTimeException):
            print("INCORRECT_INPUT")
            return
        except NoVacantRoomException:
            print("NO_VACANT_ROOM")
            return

        for available_room in available_rooms:
            print(available_room.get_meeting_room_name(), end="\t")
        print()

    def __get_time_range(self, start_time, end_time):
        time_range = Event(start_time, end_time)
        return time_range
