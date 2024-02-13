import requests
import json
import time
from config import X_RapidAPI_Host, X_RapidAPI_Key
from queries.search_everywhere import SearchEverywhere
from queries.search_flights import SearchFlights
from models.destination import Destination
from parsers.search_flights_parser import get_prices
from facade.dao_single_search import execute_dao_single_search
from dao_communication.dao_raw_request import get_new_raw_requests

while True:
    new_searches = get_new_raw_requests()
    for search in new_searches:
        parts = search["request"].split()
        execute_dao_single_search(search["chat_id"], parts[0], parts[1], [parts[2], parts[3]], [int(parts[4]), int(parts[5])])
    time.sleep(1)