from src.dao.portfolio import PortfolioDao
from src.services.portfolio_manager import PortfolioManager


class PortfolioManagerImpl(PortfolioManager):
    def __init__(self):
        self._dao = PortfolioDao.get_instance()

    def current_portfolio(self, mutual_fund_names: list[str]):
        self._dao.set_portfolio(mutual_fund_names)

    def get_current_portfolio(self):
        return self._dao.get_portfolio()

