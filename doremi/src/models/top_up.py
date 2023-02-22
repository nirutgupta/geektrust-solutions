from enum import Enum


class TopUpDeviceCategory(Enum):
    FOUR_DEVICE = 1
    TEN_DEVICE = 2


class TopUp:
    def __init__(self, device_category: TopUpDeviceCategory, duration_in_months, amount):
        self._amount = amount
        self._duration_in_months = duration_in_months
        self._device_category = device_category

    @property
    def device_category(self):
        return self._device_category

    @property
    def duration(self):
        return self._duration_in_months

    @property
    def amount(self):
        return int(self._amount)

    def get_cost(self):
        return int(self._amount)
