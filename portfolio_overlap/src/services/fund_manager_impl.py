from src.dao.mutual_fund import MutualFundDao
from src.models.stock import Stock
from src.services.fund_manager import MutualFundManager
from src.utils.constants import ROUND_PERCENT_TO_DECIMAL_PLACES, FUND_NOT_FOUND_ERROR, EXCLUDE_OVERLAP_PERCENT
from src.utils.exceptions import FundNotFoundException
from src.mutual_funds.helpers import stocks_overlap_between
from src.utils.helpers import limit_float_decimal_points


class MutualFundManagerImpl(MutualFundManager):

    def __init__(self):
        self._dao = MutualFundDao.get_instance()

    def add_stock(self, fund_name, stock_name):
        try:
            mutual_fund = self._dao.get_mutual_fund(fund_name)
            mutual_fund.add_stock(Stock(stock_name))
            self._dao.update(mutual_fund)
        except FundNotFoundException:
            print(FUND_NOT_FOUND_ERROR)

    def get_stocks(self, fund_name):
        mutual_fund = self._dao.get_mutual_fund(fund_name)
        return mutual_fund.stocks

    def find_mutual_fund_by_name(self, fund_name):
        return self._dao.get_mutual_fund(fund_name)

    def calculate_overlap(self, fund_name1, fund_name2):
        fund1 = self._dao.get_mutual_fund(fund_name1)
        fund2 = self._dao.get_mutual_fund(fund_name2)
        stock_overlap_percent = stocks_overlap_between(fund1, fund2)
        if stock_overlap_percent != EXCLUDE_OVERLAP_PERCENT:
            print(f"{fund_name1} {fund_name2} {limit_float_decimal_points(stock_overlap_percent, ROUND_PERCENT_TO_DECIMAL_PLACES)}%")
