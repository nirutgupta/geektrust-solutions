from src.models.plan import Plan
from src.utils.core import validate_date
from src.exceptions.common import InvalidDateException
from src.utils.core import get_renewal_reminder_date


class Subscription:

    def __init__(self, start_date, plan):
        self.__plan: Plan = plan
        if not validate_date(start_date):
            raise InvalidDateException()
        self.__start_date = start_date

    @property
    def start_date(self):
        return self.__start_date

    @property
    def plan(self):
        return self.__plan

    def get_renewal_reminder_date(self):
        plan_duration_in_months = self.__plan.duration
        date = get_renewal_reminder_date(self.__start_date, plan_duration_in_months)
        return date

    def get_cost(self):
        return int(self.__plan.get_cost())

    def get_plan_streaming_category(self):
        return self.__plan.streaming_category
