from dataclasses import dataclass, field


@dataclass
class AmountDeductedBreakdown:
    fare: int
    extra_fees: int
    total: int = field(init=False)

    def __post_init__(self):
        self.total = self.fare + self.extra_fees
