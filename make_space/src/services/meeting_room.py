from typing import List

from src.constants import MeetingRoomSize, MeetingRoomName
from src.exceptions import NoVacantRoomException
from src.models.meeting.room import MeetingRoom
from src.models.room import Room


class MeetingRoomFinder:
    def find_available_rooms(self, meeting_rooms, time_range):
        available_rooms = []
        for meeting_room in meeting_rooms:
            if self.__is_room_available(meeting_room, time_range):
                available_rooms.append(meeting_room)
        return available_rooms

    @staticmethod
    def __is_room_available(meeting_room, time_range):
        events = meeting_room.get_events()
        for event in events:
            if event.overlap(time_range):
                return False
        return True


class MeetingRoomService:

    def __init__(self):
        self.__meeting_room_finder = MeetingRoomFinder()
        self.__meeting_rooms = [
            MeetingRoom(Room(MeetingRoomName.CAVE, MeetingRoomSize.CAVE)),
            MeetingRoom(Room(MeetingRoomName.TOWER, MeetingRoomSize.TOWER)),
            MeetingRoom(Room(MeetingRoomName.MANSION, MeetingRoomSize.MANSION))
        ]

    @staticmethod
    def __validate_rooms(rooms):
        if len(rooms) == 0:
            raise NoVacantRoomException()

    def get_meeting_rooms(self, time_range):
        available_rooms: List[MeetingRoom] = self.__meeting_room_finder.find_available_rooms(self.__meeting_rooms,
                                                                                             time_range)
        self.__validate_rooms(available_rooms)
        return available_rooms

    def __get_meeting_rooms_with_capacity(self, time_range, person_capacity):
        available_rooms: List[MeetingRoom] = self.get_meeting_rooms(time_range)
        available_rooms_with_capacity = []
        for available_room in available_rooms:
            if available_room.get_meeting_room_capacity() >= person_capacity:
                available_rooms_with_capacity.append(available_room)
        self.__validate_rooms(available_rooms_with_capacity)
        return available_rooms_with_capacity

    def get_meeting_room(self, time_range, person_capacity):
        available_rooms_with_capacity = self.__get_meeting_rooms_with_capacity(time_range, person_capacity)
        return available_rooms_with_capacity[0]

    def create_event(self, meeting_room, time_range):
        meeting_room.add_event(time_range)
