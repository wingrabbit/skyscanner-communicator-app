import requests
import ast
import json

from tasks.task_factory import generate_tasks
from service.execute_tasks import execute_task
from parsers.search_flights_parser import get_search_result, get_prices

from dao_communication.dao_city import get_city
from dao_communication.dao_search import get_search
from dao_communication.dao_result import insert_results
from dao_communication.dao_price import insert_price
from dao_communication.dao_raw_request import update_raw_request

def execute_dao_single_search(user_id, city_from, city_to, date_range, days_range, raw_search_id=None):
    destination_from = get_city(city_from)
    destination_to = get_city(city_to)

    global_task = get_search(user_id, destination_from, destination_to, date_range, days_range)
    update_raw_request(raw_search_id, "IN PROGRESS", global_task.id)

    tasks = generate_tasks(global_task)
    insert_results(tasks)

    for task in tasks:
        print(task)
        try:
            task_result = execute_task(task)
            data = ast.literal_eval(json.dumps(task_result))
            unformatted_prices = get_prices(ast.literal_eval(data))
            final_search_result = get_search_result(task, unformatted_prices)
        except Exception as e:
            print(f'Could not execute {str(task)}, {e}')
        try:
            insert_price(final_search_result)
        except Exception as e:
            print(f'Could not insert {str(final_search_result)}, {e}')
    
    update_raw_request(raw_search_id, "DONE", global_task.id)

    print(f'Job {global_task.id} finished, {len(tasks)} tasks executed')