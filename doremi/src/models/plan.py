import abc

from abc import abstractmethod
from enum import Enum

from src.models.streaming_categories import StreamingCategory


class PlanType(Enum):
    FREE = 1
    PERSONAL = 2
    PREMIUM = 3


class IPlan(abc.ABC):

    @property
    @abstractmethod
    def streaming_category(self):
        pass

    @property
    @abstractmethod
    def plan_type(self):
        pass

    @property
    @abstractmethod
    def duration(self):
        pass

    @property
    @abstractmethod
    def amount(self):
        pass


class Plan(IPlan):

    def __init__(self, streaming_category:  StreamingCategory, plan_type: PlanType, duration, amount):
        self._streaming_category = streaming_category
        self._plan_type = plan_type
        self._duration = duration
        self._amount = amount

    @property
    def streaming_category(self):
        return self._streaming_category

    @property
    def plan_type(self):
        return self._plan_type

    @property
    def duration(self):
        return self._duration

    @property
    def amount(self):
        return self._amount

    def get_cost(self):
        return int(self._amount)
