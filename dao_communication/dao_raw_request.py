import requests
from config import DAO_server_URL, DAO_raw_requests_URL

def get_new_raw_requests():
    url = f"{DAO_server_URL}{DAO_raw_requests_URL}"
    attempt = requests.get(url)
    result_json = attempt.json()
    return result_json