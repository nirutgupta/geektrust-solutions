from src.services.make_space import MakeSpaceService


class MakeSpaceFacade:
    def __init__(self):
        self.__make_space_service = MakeSpaceService()

    def book(self, start_time, end_time, person_capacity):
        self.__make_space_service.create_booking(start_time, end_time, person_capacity)

    def vacancy(self, start_time, end_time):
        self.__make_space_service.get_available_rooms(start_time, end_time)
