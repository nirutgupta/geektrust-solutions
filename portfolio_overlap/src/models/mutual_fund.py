from dataclasses import dataclass

from src.models.stock import Stock


@dataclass
class MutualFund:
    name: str
    stocks: list[Stock]
    OVERLAP_NUMERATOR = 2
    HUNDRED = 100

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)

    @property
    def no_of_stocks(self):
        return len(self.stocks)

    def overlap(self, other: 'MutualFund') -> float:
        return self.OVERLAP_NUMERATOR*len(set(self.stocks).intersection(other.stocks))/(len(self.stocks)+len(other.stocks)) * self.HUNDRED
