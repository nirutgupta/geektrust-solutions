from typing import List

from src.models.portfolio import Portfolio


class PortfolioDao:
    """
    Singleton class for get/set portfolio
    """
    __instance = None

    def __init__(self):
        self._portfolio: Portfolio = Portfolio()

    @staticmethod
    def get_instance() -> 'PortfolioDao':
        if PortfolioDao.__instance is None:
            PortfolioDao.__instance = PortfolioDao()
        return PortfolioDao.__instance

    def set_portfolio(self, mutual_funds: List[str]):
        for mutual_fund in mutual_funds:
            self._portfolio.add_mutual_fund_name(mutual_fund)

    def get_portfolio(self):
        return self._portfolio.get_mutual_fund_names()
