from src.models.point import Point


class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._board = [[Point(row, col) for col in range(self._columns)] for row in range(self._rows, -1, -1)]
