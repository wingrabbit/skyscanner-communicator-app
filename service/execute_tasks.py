from tasks.task import Task
from models.destination import Destination
from queries.search_flights import SearchFlights

def execute_task(task: Task):
    return str(SearchFlights(task.origin, task.destination, task.date_to, task.date_return).execute())