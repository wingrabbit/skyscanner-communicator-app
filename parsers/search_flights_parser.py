import json
from models.search_result import SearchResult
from tasks.task import Task, Destination

def get_prices(flight_json):
    return flight_json['data']['filterStats']['stopPrices']

def extract_price_if_exists(unformatted_price):
    if unformatted_price['isPresent']==False:
        return None
    return int(''.join(i for i in unformatted_price['formattedPrice'] if i.isdigit()))

def get_search_result(task: Task, unformatted_prices) -> SearchResult:
    return SearchResult(
        task.origin.title,
        task.destination.title,
        str(task.date_to),
        str(task.date_return),
        extract_price_if_exists(unformatted_prices['direct']),
        extract_price_if_exists(unformatted_prices['one']),
        extract_price_if_exists(unformatted_prices['twoOrMore'])
    )