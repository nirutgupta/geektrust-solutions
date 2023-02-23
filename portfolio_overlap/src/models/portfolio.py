from dataclasses import dataclass, field
from typing import List


@dataclass
class Portfolio:
    _mutual_fund_names: List[str] = field(init=False, default_factory=list)

    def add_mutual_fund_name(self, fund_name):
        self._mutual_fund_names.append(fund_name)

    def get_mutual_fund_names(self):
        return self._mutual_fund_names
