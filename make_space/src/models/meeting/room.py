from src.constants import BufferedTime
from src.models.meeting.calendar import MeetingCalendar
from src.models.room import Room
from src.models.event import Event


class MeetingRoom:
    _buffer_times = [
        Event(BufferedTime.MORNING_START, BufferedTime.MORNING_END),
        Event(BufferedTime.AFTERNOON_START, BufferedTime.AFTERNOON_END),
        Event(BufferedTime.EVENING_START, BufferedTime.EVENING_END)
    ]

    def __init__(self, room: Room):
        self._room = room
        self._calendar = MeetingCalendar()
        self._calendar.add_events(self._buffer_times)

    def add_event(self, time_range):
        self._calendar.add_event(time_range)

    def get_events(self):
        return self._calendar.get_events()

    def get_meeting_room_name(self):
        return self._room.name

    def get_meeting_room_capacity(self):
        return self._room.capacity
