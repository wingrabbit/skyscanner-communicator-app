from queries.general_query import GeneralQuery
from config import search_everywhere_URL

class SearchEverywhere(GeneralQuery):
    def __init__(self, origin_sky_id, travel_date) -> None:
        self.url += search_everywhere_URL
        self.query_string = {"originSkyId": origin_sky_id,"travelDate": travel_date}

    