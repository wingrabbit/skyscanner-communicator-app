import requests
import time
from config import DAO_server_URL, DAO_city_URL
from models.destination import Destination
from queries.search_destination import SearchDestination
from parsers.search_destination_parser import get_destination

def get_city(city_name) -> Destination:
    url = f"{DAO_server_URL}{DAO_city_URL}?name={city_name}"
    attempt = requests.get(url)
    if(attempt.json()["id"]==-1):
        destination = get_destination(SearchDestination(city_name).execute())
        city_json = {"name": destination.title, "sky_id": destination.sky_id, "entity_id": destination.entity_id}
        attempt = requests.post(url, json=city_json)
        time.sleep(1)
    result_json = attempt.json()
    result = Destination(id=result_json["id"], entity_id=result_json["entity_id"], title=result_json["name"], sky_id=result_json["sky_id"])
    return result