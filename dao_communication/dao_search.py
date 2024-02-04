import requests
from config import DAO_server_URL, DAO_search_URL
from tasks.global_task import GlobalTask
from models.destination import Destination

def get_search(user_id, city_from: Destination, city_to: Destination, dates_range: list[str], days_range: list[int]) -> GlobalTask:
    url=f'{DAO_server_URL}{DAO_search_URL}'
    search_json = {"user_id": user_id, "city_from_id":city_from.id, "city_to_id": city_to.id, "date_min": dates_range[0], "date_max": dates_range[1], "days_min": days_range[0], "days_max": days_range[1]}
    attempt = requests.post(url, json=search_json)
    result_json = attempt.json()
    result = GlobalTask(city_from, city_to, dates_range, days_range, id=result_json["id"], user_id=user_id)
    return result