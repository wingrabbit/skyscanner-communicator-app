from queries.general_query import GeneralQuery
from models.destination import Destination
from config import search_flights_URL


class SearchFlights(GeneralQuery):

    def __init__(self, origin: Destination, destination: Destination, date_to, date_return=None) -> None:
        self.url += search_flights_URL
        self.query_string = {"originSkyId": origin.sky_id,
                             "destinationSkyId": destination.sky_id,
                             "originEntityId": origin.entity_id,
                             "destinationEntityId": destination.entity_id,
                             "date": date_to,
                             "returnDate": date_return,
                             "adults": "1",
                             "currency": "CAD",
                             "market": "en-US",
                             "countryCode": "CA"}
