import requests
from config import X_RapidAPI_Host, X_RapidAPI_Key
from queries.search_everywhere import SearchEverywhere

s = SearchEverywhere("JFK", "2023-11-08")
print(s.execute())