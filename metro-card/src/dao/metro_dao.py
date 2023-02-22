import copy

from collections import defaultdict

from src.exceptions.no_metro_card_exception import NoMetroCardFoundException
from src.models.metro_card import MetroCard


class MetroDao:
    __instance = None

    def __init__(self):
        self.cards: dict[str, MetroCard] = {}
        self.stations_to_collection = defaultdict(int)
        self.stations_to_discount = defaultdict(int)
        self.stations_to_passengers = {}

    @staticmethod
    def get_instance():
        if not MetroDao.__instance:
            MetroDao.__instance = MetroDao()
        return MetroDao.__instance

    def add_card(self, metro_card: MetroCard):
        self.cards[metro_card.number] = metro_card
        # print("Added card successfully!")

    def get_card(self, metro_card_number) -> MetroCard:
        if not self.cards.get(metro_card_number):
            raise NoMetroCardFoundException(f"No Metro card with {metro_card_number} found!")
        return copy.deepcopy(self.cards[metro_card_number])

    def deduct_from_card(self, metro_card_number, fare):
        card = self.cards[metro_card_number]
        card.deduct(fare)
        return True

    def add_trip_to_card(self, metro_card_number, trip):
        card = self.cards[metro_card_number]
        card.add_trip(trip)

    def add_balance_to_card(self, metro_card_number, balance):
        card = self.cards[metro_card_number]
        card.add_balance(balance)

    def add_collection(self, station, collection):
        self.stations_to_collection[station] += collection

    def add_discount(self, station, discount):
        self.stations_to_discount[station] += discount

    def add_passenger(self, station, passenger_type):
        if station not in self.stations_to_passengers:
            self.stations_to_passengers[station] = {}
        if passenger_type not in self.stations_to_passengers[station]:
            self.stations_to_passengers[station][passenger_type] = 1
        else:
            self.stations_to_passengers[station][passenger_type] += 1

    def get_collection(self, station):
        return self.stations_to_collection[station]

    def get_discount(self, station):
        return self.stations_to_discount[station]

    def get_passenger(self, station):
        return self.stations_to_passengers[station]
