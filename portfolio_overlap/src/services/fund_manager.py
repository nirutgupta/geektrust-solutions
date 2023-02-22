from abc import abstractmethod, ABC


class MutualFundManager(ABC):
    @abstractmethod
    def add_stock(self, fund_name, stock_name):
        ...

    @abstractmethod
    def get_stocks(self, fund_name):
        ...

    @abstractmethod
    def find_mutual_fund_by_name(self, fund_name):
        ...

    @abstractmethod
    def calculate_overlap(self, fund_name1, fund_name2):
        ...
