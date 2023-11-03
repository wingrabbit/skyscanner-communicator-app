import requests
import json
from config import X_RapidAPI_Host, X_RapidAPI_Key
from queries.search_everywhere import SearchEverywhere
from queries.search_flights import SearchFlights
from models.destination import Destination
from parsers.search_flights_parser import get_prices

#s = SearchEverywhere("JFK", "2023-11-08")
#s = SearchFlights(Destination("LOND", "27544008"), Destination("NYCA", "27537542"), "2024-02-20", "2024-02-23")
with open('sample_responses/search_flights.json', 'r') as f:
    data = json.load(f)
    print(get_prices(data))
    
    
#print(s.execute())