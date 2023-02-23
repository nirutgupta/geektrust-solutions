import copy
from typing import List, Optional

from src.enums.streaming_category import StreamingCategory
from src.models.plan import PlanType, Plan
from src.models.subscription import Subscription
from src.models.subscription_top_up import SubscriptionTopUp
from src.models.top_up import TopUpDeviceCategory, TopUp
from src.utils.constants import FREE_PLAN_DURATION_IN_MONTHS, PERSONAL_PLAN_DURATION_IN_MONTHS, \
    PREMIUM_PLAN_DURATION_IN_MONTHS, TOPUP_DURATION_IN_MONTHS, PlanCost, TopUpCost


class DoremiDAO:
    __instance = None

    def __init__(self):
        self.__start_subscription = ""
        self.__topup: Optional[SubscriptionTopUp] = None
        self.__plans = {
            StreamingCategory.MUSIC.name: {
                PlanType.FREE.name: Plan(StreamingCategory.MUSIC, PlanType.FREE, FREE_PLAN_DURATION_IN_MONTHS, PlanCost.FREE_PLAN_COST),
                PlanType.PERSONAL.name: Plan(StreamingCategory.MUSIC, PlanType.PERSONAL, PERSONAL_PLAN_DURATION_IN_MONTHS, PlanCost.MUSIC_PERSONAL),
                PlanType.PREMIUM.name: Plan(StreamingCategory.MUSIC, PlanType.PREMIUM,PREMIUM_PLAN_DURATION_IN_MONTHS, PlanCost.MUSIC_PREMIUM)
            },
            StreamingCategory.VIDEO.name: {
                PlanType.FREE.name: Plan(StreamingCategory.VIDEO, PlanType.FREE, FREE_PLAN_DURATION_IN_MONTHS, PlanCost.FREE_PLAN_COST),
                PlanType.PERSONAL.name: Plan(StreamingCategory.VIDEO, PlanType.PERSONAL, PERSONAL_PLAN_DURATION_IN_MONTHS, PlanCost.VIDEO_PERSONAL),
                PlanType.PREMIUM.name: Plan(StreamingCategory.VIDEO, PlanType.PREMIUM, PREMIUM_PLAN_DURATION_IN_MONTHS, PlanCost.VIDEO_PREMIUM)
            },
            StreamingCategory.PODCAST.name: {
                PlanType.FREE.name: Plan(StreamingCategory.PODCAST, PlanType.FREE, FREE_PLAN_DURATION_IN_MONTHS, PlanCost.FREE_PLAN_COST),
                PlanType.PERSONAL.name: Plan(StreamingCategory.PODCAST, PlanType.PERSONAL, PERSONAL_PLAN_DURATION_IN_MONTHS, PlanCost.PODCAST_PERSONAL),
                PlanType.PREMIUM.name: Plan(StreamingCategory.PODCAST, PlanType.PREMIUM, PREMIUM_PLAN_DURATION_IN_MONTHS, PlanCost.PODCAST_PREMIUM)
            }
        }
        self.__top_ups = {
            TopUpDeviceCategory.FOUR_DEVICE.name: TopUp(TopUpDeviceCategory.FOUR_DEVICE, TOPUP_DURATION_IN_MONTHS, TopUpCost.FOUR_DEVICE),
            TopUpDeviceCategory.TEN_DEVICE.name: TopUp(TopUpDeviceCategory.TEN_DEVICE, TOPUP_DURATION_IN_MONTHS, TopUpCost.TEN_DEVICE)
        }
        self.__subscriptions = []

    @staticmethod
    def get_instance():
        if DoremiDAO.__instance is None:
            DoremiDAO.__instance = DoremiDAO()
        return DoremiDAO.__instance

    def set_start_subscription_date(self, date):
        self.__start_subscription = date

    def get_start_subscription_date(self):
        return self.__start_subscription

    def add_subscription(self, subscription):
        self.__subscriptions.append(subscription)

    def get_plan(self, streaming_category, plan_type):
        return copy.deepcopy(self.__plans[streaming_category][plan_type])

    def get_topup(self):
        return self.__topup

    def set_topup(self, topup: SubscriptionTopUp):
        self.__topup = topup

    def get_subscriptions(self) -> List[Subscription]:
        return copy.deepcopy(self.__subscriptions)

    def get_topup_from_topups(self, devices):
        return copy.deepcopy(self.__top_ups[devices])
