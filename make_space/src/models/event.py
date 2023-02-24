from dataclasses import dataclass

from src.constants import MINUTE_INTERVAL
from src.exceptions import IncorrectTimeRangeException, IncorrectTimeException
from src.utils import str_to_datetime


@dataclass(frozen=True)
class Event:
    start: str
    end: str

    def __post_init__(self):
        self.__validate_time_range()

    def __validate_time_range(self):
        start_date = str_to_datetime(self.start)
        end_date = str_to_datetime(self.end)
        self.__validate_end_greater_than_start(start_date, end_date)
        self.__validate_time_interval(start_date)
        self.__validate_time_interval(end_date)

    @staticmethod
    def __validate_end_greater_than_start(start_date, end_date):
        if start_date >= end_date:
            raise IncorrectTimeRangeException()

    @staticmethod
    def __validate_time_interval(date):
        if date.minute % MINUTE_INTERVAL != 0:
            raise IncorrectTimeException()

    def overlap(self, other: 'Event') -> bool:
        if max(self.start, other.start) < min(self.end, other.end):
            return True
        return False
