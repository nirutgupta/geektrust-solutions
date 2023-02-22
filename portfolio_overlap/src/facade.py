from src.services.fund_manager_impl import MutualFundManagerImpl
from src.services.portfolio_manager_impl import PortfolioManagerImpl
from src.utils.constants import FUND_NOT_FOUND_ERROR
from src.utils.exceptions import FundNotFoundException


class PortfolioOverlapFacade:
    def __init__(self):
        self.portfolio_manager = PortfolioManagerImpl()
        self.fund_manager = MutualFundManagerImpl()

    def current_portfolio(self, args):
        self.portfolio_manager.current_portfolio(args)

    def calculate_overlap(self, fund_name):
        try:
            self.fund_manager.find_mutual_fund_by_name(fund_name)
        except FundNotFoundException:
            print(FUND_NOT_FOUND_ERROR)
        else:
            for portfolio_fund_name in self.portfolio_manager.get_current_portfolio():
                self.fund_manager.calculate_overlap(fund_name, portfolio_fund_name)

    def add_stock(self, fund_name, stock_name):
        self.fund_manager.add_stock(fund_name, stock_name)
