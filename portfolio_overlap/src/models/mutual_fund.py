from dataclasses import dataclass

from src.models.stock import Stock


@dataclass
class MutualFund:
    name: str
    stocks: list[Stock]

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)

    @property
    def no_of_stocks(self):
        return len(self.stocks)
