from dataclasses import dataclass


@dataclass(frozen=True)
class Stock:
    _name: str

    @property
    def name(self):
        return self._name
