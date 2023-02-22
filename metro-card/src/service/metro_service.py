from src.dao.metro_dao import MetroDao
from src.models.metro_card import MetroCard
from src.models.passenger_type import PassengerType
from src.models.trip import Trip
from src.service.payment_service import PaymentService
from src.service.trip_fare_service import TripFareService
from src.view.station_view import StationSummary


class MetroService:
    def __init__(self):
        self.dao: MetroDao = MetroDao.get_instance()
        self.payments = PaymentService()

    def init_metro_card(self, card_number, balance):
        new_metro_card = MetroCard(card_number, int(balance))
        self.dao.add_card(new_metro_card)

    def check_in(self, card_number, passenger_type, station):
        passenger_type = getattr(PassengerType, passenger_type)
        card = self.dao.get_card(card_number)
        fare = TripFareService.calculate_fare(card, passenger_type.name, station)
        trip = Trip(passenger_type=passenger_type, source=station)
        if fare.charged_fare < fare.actual_fare:
            trip.return_trip = True
        breakdown = self.payments.deduct_from_card(card_number, fare.charged_fare)
        self.dao.add_trip_to_card(card_number, trip)
        self.dao.add_collection(station, breakdown.total)
        self.dao.add_discount(station, fare.actual_fare-fare.charged_fare)
        self.dao.add_passenger(station, passenger_type.name)

    def print_summary(self):
        stations = ["CENTRAL", "AIRPORT"]

        for station in stations:
            StationSummary.print_summary(
                station,
                self.dao.get_collection(station),
                self.dao.get_discount(station),
                self.dao.get_passenger(station)
            )
