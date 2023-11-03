import datetime
from tasks.global_task import GlobalTask
from tasks.task import Task


def generate_tasks(global_task: GlobalTask) -> [Task]:
    result = []
    start_date = datetime.datetime.strptime(
        global_task.dates_range[0], '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(
        global_task.dates_range[1], '%Y-%m-%d').date()
    curr = start_date
    while curr <= end_date:
        for i in range(global_task.days_range[0], global_task.days_range[1]+1):
            result.append(Task(global_task.origin, global_task.destination, curr.strftime(
                '%Y-%m-%d'), (curr+datetime.timedelta(days=i)).strftime('%Y-%m-%d')))
        curr += datetime.timedelta(days=1)
    return result
