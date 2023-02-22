from abc import abstractmethod, ABC


class PortfolioManager(ABC):

    @abstractmethod
    def current_portfolio(self, mutual_funds: list[str]):
        ...

    @abstractmethod
    def get_current_portfolio(self):
        ...