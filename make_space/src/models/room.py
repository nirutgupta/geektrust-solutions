from dataclasses import dataclass


@dataclass
class Room:
    _name: str
    _capacity: int

    @property
    def name(self):
        return self._name

    @property
    def capacity(self):
        return self._capacity
