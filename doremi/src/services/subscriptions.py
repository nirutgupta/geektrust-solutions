from src.exceptions.common import InvalidDateException
from src.models.subscription import Subscription
from src.utils.core import validate_date
from src.view.viewer import Viewer

from src.dao.doremi_dao import DoremiDAO


class SubscriptionsService:
    def __init__(self):
        self.dao = DoremiDAO.get_instance()
        self.subscription = []

    def start_subscription(self, date):
        if not validate_date(date):
            Viewer.print_string("INVALID_DATE")
        self.dao.set_start_subscription_date(date)

    def get_start_subscription(self):
        return self.dao.get_start_subscription_date()

    def __check_duplicate_subscription(self, streaming_category) -> bool:
        subs = self.dao.get_subscriptions()
        for sub in subs:
            if sub.get_plan_streaming_category().name == streaming_category:
                return True
        return False

    def add_subscription(self, streaming_category, plan_type):
        if self.__check_duplicate_subscription(streaming_category):
            Viewer.print_string("ADD_SUBSCRIPTION_FAILED\tDUPLICATE_CATEGORY")
            return

        plan = self.dao.get_plan(streaming_category, plan_type)
        try:
            subscription = Subscription(self.dao.get_start_subscription_date(), plan)
            self.dao.add_subscription(subscription)
        except InvalidDateException:
            Viewer.print_string("ADD_SUBSCRIPTION_FAILED\tINVALID_DATE")

    def add_topup(self, devices, duration):
        if self.dao.get_topup():
            Viewer.print_string("ADD_TOPUP_FAILED\tDUPLICATE_TOPUP")
            return
        if not validate_date(self.dao.get_start_subscription_date()):
            Viewer.print_string("ADD_TOPUP_FAILED\tINVALID_DATE")
            return
        if len(self.dao.get_subscriptions()) == 0:
            Viewer.print_string("ADD_TOPUP_FAILED\tSUBSCRIPTIONS_NOT_FOUND")
            return
        topup = self.dao.get_topup_from_topups(devices)
        self.dao.set_topup((topup, int(duration)))

    def print_renewal_details(self):
        subs = self.dao.get_subscriptions()
        if len(subs) == 0:
            Viewer.print_string("SUBSCRIPTIONS_NOT_FOUND")
            return
        renewal_reminders = []
        renewal_amount = 0
        for sub in subs:
            renewal_amount += sub.get_cost()
            renewal_reminders.append((sub.get_plan_streaming_category(), sub.get_renewal_reminder_date()))
        if self.dao.get_topup():
            topup, duration = self.dao.get_topup()
            renewal_amount += ((topup.get_cost())*duration)
        Viewer.print_renewal_details(renewal_reminders, renewal_amount)
