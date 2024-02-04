import requests
from config import DAO_server_URL, DAO_price_URL
from models.search_result import SearchResult

def insert_price(price: SearchResult):
    url = f"{DAO_server_URL}{DAO_price_URL}"
    if price.direct is not None:
        result_json = price_json = {"result_id": price.result_id, "price":price.direct, "stops": "0"}
        attempt = requests.post(url, json=result_json)
    if price.one is not None:
        result_json = price_json = {"result_id": price.result_id, "price":price.one, "stops": "1"}
        attempt = requests.post(url, json=result_json)
    if price.two_plus is not None:
        result_json = price_json = {"result_id": price.result_id, "price":price.two_plus, "stops": "2"}
        attempt = requests.post(url, json=result_json)
    