from src.exceptions.common import InvalidDateException, DuplicateTopUpException, SubscriptionsNotFoundException, \
    DuplicateSubscriptionException
from src.models.subscription import Subscription
from src.models.subscription_top_up import SubscriptionTopUp
from src.utils.core import validate_date
from src.validators.subscriptions import SubscriptionsValidator
from src.view.viewer import Viewer

from src.dao.doremi_dao import DoremiDAO


class SubscriptionsService:
    def __init__(self):
        self.dao = DoremiDAO.get_instance()
        self.__validator = SubscriptionsValidator(self.dao)

    def start_subscription(self, date):
        if not validate_date(date):
            Viewer.print_string("INVALID_DATE")
        self.dao.set_start_subscription_date(date)

    def add_subscription(self, streaming_category, plan_type):
        try:
            self.__validator.validate_duplicate_subscription(streaming_category)
            self.__validator.validate_subscription_date()
        except DuplicateSubscriptionException:
            Viewer.print_string("ADD_SUBSCRIPTION_FAILED\tDUPLICATE_CATEGORY")
            return
        except InvalidDateException:
            Viewer.print_string("ADD_SUBSCRIPTION_FAILED\tINVALID_DATE")
            return

        plan = self.dao.get_plan(streaming_category, plan_type)
        subscription = Subscription(self.dao.get_start_subscription_date(), plan)
        self.dao.add_subscription(subscription)

    def add_topup(self, devices, duration):
        try:
            self.__validator.validate_subscription_date()
            self.__validator.validate_subscription_exists()
            self.__validator.validate_duplicate_topup()
        except InvalidDateException:
            Viewer.print_string("ADD_TOPUP_FAILED\tINVALID_DATE")
            return
        except SubscriptionsNotFoundException:
            Viewer.print_string("ADD_TOPUP_FAILED\tSUBSCRIPTIONS_NOT_FOUND")
            return
        except DuplicateTopUpException:
            Viewer.print_string("ADD_TOPUP_FAILED\tDUPLICATE_TOPUP")
            return

        topup = self.dao.get_topup_from_topups(devices)
        self.dao.set_topup(SubscriptionTopUp(topup, int(duration)))

    def print_renewal_details(self):
        try:
            self.__validator.validate_subscription_exists()
        except SubscriptionsNotFoundException:
            Viewer.print_string("SUBSCRIPTIONS_NOT_FOUND")
            return

        renewal_reminders = []
        renewal_amount = 0
        subs = self.dao.get_subscriptions()
        for sub in subs:
            renewal_amount += sub.get_cost()
            renewal_reminders.append((sub.get_plan_streaming_category(), sub.get_renewal_reminder_date()))
        if self.dao.get_topup():
            subscription_topup = self.dao.get_topup()
            renewal_amount += subscription_topup.get_cost()
        Viewer.print_renewal_details(renewal_reminders, renewal_amount)
