from typing import Optional

from src.enums.direction import Direction
from src.gman.game import Game
from src.models.point import Point


class GManFacade:
    def __init__(self):
        self._source_point: Optional[Point] = None
        self._source_direction: Optional[Direction] = None
        self._destination: Optional[Point] = None
        self._game: Game = Game()

    def source(self, *args):
        self._source_point = Point(int(args[0]), int(args[1]))
        self._source_direction = getattr(Direction, args[2])

    def destination(self, *args):
        self._destination = Point(int(args[0]), int(args[1]))

    def print_power(self):
        self._game.play(self._source_point, self._source_direction, self._destination)
        power = self._game.print_power()
        print(f"POWER {power}")
