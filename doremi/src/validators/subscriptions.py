from src.exceptions.common import DuplicateSubscriptionException, DuplicateTopUpException, \
    SubscriptionsNotFoundException, InvalidDateException
from src.utils.core import validate_date


class SubscriptionsValidator:
    def __init__(self, dao):
        self.dao = dao

    def validate_duplicate_subscription(self, streaming_category):
        subs = self.dao.get_subscriptions()
        for sub in subs:
            if sub.get_plan_streaming_category().name == streaming_category:
                raise DuplicateSubscriptionException()

    def validate_duplicate_topup(self):
        if self.dao.get_topup():
            raise DuplicateTopUpException()

    def validate_subscription_exists(self):
        if len(self.dao.get_subscriptions()) == 0:
            raise SubscriptionsNotFoundException()

    def validate_subscription_date(self):
        if not validate_date(self.dao.get_start_subscription_date()):
            raise InvalidDateException
