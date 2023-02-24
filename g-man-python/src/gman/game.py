from src.constants import GMAN_MAX_POWER
from src.enums.direction import Direction
from src.models.gman import GMan
from src.gman.path_finder import PathFinder
from src.models.point import Point


class Game:
    def __init__(self):
        self._gman = None
        self.__path_finder = PathFinder()

    def initialize_gman(self, source, source_direction):
        self._gman = GMan(GMAN_MAX_POWER, source, source_direction)

    def play(self, source: Point, source_direction: Direction, destination: Point):
        self.initialize_gman(source, source_direction)
        moves = self.__path_finder.get_no_of_moves(source, destination)
        turns = self.__path_finder.get_no_of_turns(source, source_direction, destination)

        for move in range(moves):
            self._gman.move()

        for turn in range(turns):
            self._gman.turn()

    def print_power(self):
        if not self._gman:
            raise Exception("Game not played yet!")
        return self._gman.power
