import requests
from config import DAO_server_URL, DAO_result_URL
from tasks.task import Task

def insert_results(tasks: [Task]):
    url = f"{DAO_server_URL}{DAO_result_URL}"
    for task in tasks:
        result_json = {"search_id": task.search_id, "date_from":task.date_to, "date_return": task.date_return}
        attempt = requests.post(url, json=result_json)
        #print(attempt)
        task.id = attempt.json()["id"]
        #print(task)