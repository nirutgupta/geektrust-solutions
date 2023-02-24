from src.enums.direction import Direction


class PathFinder:
    @staticmethod
    def get_no_of_moves(source, destination):
        moves = abs(source.y - destination.y) + abs(source.x - destination.x)
        return moves

    @staticmethod
    def get_no_of_turns(source, source_direction, destination):
        relative_directions_to_destination = [
            PathFinder.__get_relative_x_direction(source, destination),
            PathFinder.__get_relative_y_direction(source, destination)
        ]
        return PathFinder.__get_turns_from_relative_directions(relative_directions_to_destination, source_direction)

    @staticmethod
    def __get_turns_from_relative_directions(relative_directions_to_destination, source_direction):
        if source_direction in relative_directions_to_destination:
            turns = 1
        else:
            turns = 2
        return turns

    @staticmethod
    def __get_relative_x_direction(source, destination):
        if source.x > destination.x:
            return Direction.W
        return Direction.E

    @staticmethod
    def __get_relative_y_direction(source, destination):
        if source.y > destination.y:
            return Direction.S
        return Direction.N
