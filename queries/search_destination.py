from queries.general_query import GeneralQuery
from config import search_airport_URL

class SearchDestination(GeneralQuery):
    def __init__(self, destination_name) -> None:
        self.url+=search_airport_URL
        self.query_string = {"query": destination_name}