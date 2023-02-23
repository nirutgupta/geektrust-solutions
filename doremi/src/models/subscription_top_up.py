from src.models.top_up import TopUp


class SubscriptionTopUp:
    def __init__(self, topup: TopUp, period):
        self._topup = topup
        self._period = period

    def get_period(self):
        return self._period

    def get_cost(self):
        return self._topup.get_cost() * self._period
