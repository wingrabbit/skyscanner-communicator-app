import ast
import json
import time

from models.destination import Destination
from models.search_result import SearchResult

from queries.search_destination import SearchDestination

from parsers.search_destination_parser import get_destination
from parsers.search_flights_parser import get_search_result, get_prices

from tasks.global_task import GlobalTask
from tasks.task import Task
from tasks.task_factory import generate_tasks

from service.execute_tasks import execute_task


def execute_single_search(city_from: str, city_to: str, dates_range: [str], days_range: [str]):
    destination_from = get_destination(SearchDestination(city_from).execute())
    time.sleep(1)
    destination_to = get_destination(SearchDestination(city_to).execute())
    time.sleep(1)

    tasks = generate_tasks(GlobalTask(destination_from, destination_to, dates_range, days_range))

    price_list = []

    tasks_count = len(tasks)
    counter = 0

    for task in tasks:
        counter+=1
        print('Executing task ', counter, '/', tasks_count)
        task_result = execute_task(task)
        data = ast.literal_eval(json.dumps(task_result))
        unformatted_prices = get_prices(ast.literal_eval(data))
        final_search_result = get_search_result(task, unformatted_prices)
        price_list.append(final_search_result)
        print(final_search_result)

    return price_list