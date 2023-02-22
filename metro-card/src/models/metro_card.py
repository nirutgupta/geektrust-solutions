from abc import abstractmethod
from typing import List

from src.exceptions.insufficient_balance import InsufficientBalance
from src.exceptions.no_last_trip_found_exception import NoLastTripFoundException
from src.models.trip import Trip


class Card:
    @property
    @abstractmethod
    def number(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def deduct(self, value):
        pass


class MetroCard(Card):
    def __init__(self, number, balance):
        self._number = number
        self._balance = balance
        self.__trips: List[Trip] = []

    @property
    def number(self):
        return self._number

    @property
    def balance(self):
        return self._balance

    def deduct(self, value):
        if value > self._balance:
            raise InsufficientBalance(f"requested for {value}, current balance is {self._balance}")
        self._balance -= value

    def get_last_trip(self) -> Trip:
        if not self.__trips:
            raise NoLastTripFoundException("No trips exists")
        return self.__trips[-1]

    def add_trip(self, trip: Trip):
        self.__trips.append(trip)

    def add_balance(self, amount):
        self._balance += amount
