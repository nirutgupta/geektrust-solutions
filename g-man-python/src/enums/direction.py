from enum import Enum


class Direction(Enum):
    S = (0, -1)
    N = (0, 1)
    W = (-1, 0)
    E = (1, 0)
