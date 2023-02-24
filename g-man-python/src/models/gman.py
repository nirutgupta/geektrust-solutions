from src.enums.direction import Direction
from src.models.bot import Bot
from src.models.point import Point


class GMan(Bot):
    def __init__(self, power, position: Point, direction: Direction):
        super().__init__(power, position, direction)
