from typing import List


class PortfolioDao:
    __instance = None

    def __init__(self):
        self._portfolio: List[str] = []

    @staticmethod
    def get_instance() -> 'PortfolioDao':
        if PortfolioDao.__instance is None:
            PortfolioDao.__instance = PortfolioDao()
        return PortfolioDao.__instance

    def set_portfolio(self, mutual_funds):
        self._portfolio = mutual_funds

    def get_portfolio(self):
        return self._portfolio
