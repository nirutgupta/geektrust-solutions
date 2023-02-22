from src.exceptions.no_last_trip_found_exception import NoLastTripFoundException
from src.models.trip_fare import TripFare
from src.utils.constants import TravelCharges


class TripFareService:
    @staticmethod
    def calculate_fare(card, passenger_type, station):
        try:
            trip = card.get_last_trip()
        except NoLastTripFoundException:
            trip = None

        discount = TripFareService.__calculate_discount(trip, passenger_type, station)

        actual_charge = getattr(TravelCharges, passenger_type)
        trip_charge = actual_charge - int(actual_charge*discount/100)

        return TripFare(actual_charge, trip_charge)

    @staticmethod
    def __calculate_discount(trip, passenger_type, station):
        discount = 0
        if not trip:
            return discount
        if trip.source != station and trip.passenger_type.name == passenger_type and not trip.return_trip:
            discount = 50
        return discount
