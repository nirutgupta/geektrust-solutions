from typing import List

from src.models.mutual_fund import MutualFund
from src.models.stock import Stock
from src.utils.exceptions import FundNotFoundException
from src.utils.helpers import get_json_from_url
from src.utils.constants import STOCK_DATA_URL, STOCK_DATA_FUNDS_ROOT_KEY, STOCK_DATA_FUNDS_FUND_STOCKS_KEY, \
    STOCK_DATA_FUNDS_FUND_NAME_KEY


class MutualFundDao:
    """
    Singleton class to add/get/update mutual funds
    """
    __instance = None

    def __init__(self):
        self._mutual_funds = []
        self.__init_db()

    @staticmethod
    def get_instance() -> 'MutualFundDao':
        if MutualFundDao.__instance is None:
            MutualFundDao.__instance = MutualFundDao()
        return MutualFundDao.__instance

    def __init_db(self) -> None:
        stock_data = get_json_from_url(STOCK_DATA_URL)
        for fund in MutualFundDao.__get_funds(stock_data):
            self.add_mutual_fund(fund)

    def add_mutual_fund(self, mutual_fund: MutualFund) -> None:
        self._mutual_funds.append(mutual_fund)

    @staticmethod
    def __get_funds(stock_data):
        funds = stock_data[STOCK_DATA_FUNDS_ROOT_KEY]
        for fund in funds:
            yield MutualFund(fund[STOCK_DATA_FUNDS_FUND_NAME_KEY], [Stock(stock) for stock in fund[STOCK_DATA_FUNDS_FUND_STOCKS_KEY]])

    def get_mutual_funds(self) -> List[MutualFund]:
        return self._mutual_funds

    def get_mutual_fund(self, fund_name) -> MutualFund:
        for mutual_fund in self._mutual_funds:
            if mutual_fund.name == fund_name:
                return mutual_fund
        raise FundNotFoundException()

    def update(self, mutual_fund: MutualFund):
        for index, fund in enumerate(self._mutual_funds):
            if fund.name == mutual_fund.name:
                self._mutual_funds[index] = mutual_fund
