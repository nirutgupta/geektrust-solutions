from src.dao.metro_dao import MetroDao
from src.exceptions.insufficient_balance import InsufficientBalance
from src.models.amount_deducted_breakdown import AmountDeductedBreakdown
from src.utils.constants import AUTO_RECHARGE_FEES_IN_PERCENT


class PaymentService:
    def __init__(self):
        self.card_dao = MetroDao.get_instance()

    def deduct_from_card(self, card_number, fare) -> AmountDeductedBreakdown:
        try:
            success = self.card_dao.deduct_from_card(card_number, fare)
            if success:
                return AmountDeductedBreakdown(fare, 0)
        except InsufficientBalance:
            pass
        card = self.card_dao.get_card(card_number)
        current_balance = card.balance
        remaining_balance = fare-current_balance
        fees = self.auto_recharge(card_number, remaining_balance)
        self.card_dao.deduct_from_card(card_number, fare)
        return AmountDeductedBreakdown(fare, fees)

    def auto_recharge(self, card_number, amount):
        fees = int(AUTO_RECHARGE_FEES_IN_PERCENT/100*amount)
        self.card_dao.add_balance_to_card(card_number, amount)
        return fees


