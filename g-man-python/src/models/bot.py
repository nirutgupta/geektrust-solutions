from src.constants import GMAN_TURN_POWER_USAGE, GMAN_MOVE_POWER_USAGE
from src.enums.direction import Direction
from src.models.point import Point


class Bot:
    def __init__(self, power, position: Point, direction: Direction):
        self._power = power
        self._position = position
        self._direction = direction

    @property
    def power(self):
        return self._power

    def move(self):
        self._power -= GMAN_MOVE_POWER_USAGE

    def turn(self):
        self._power -= GMAN_TURN_POWER_USAGE
