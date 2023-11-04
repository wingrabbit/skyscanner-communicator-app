from collections import deque
from tasks.task import Task

class GlobalQueue:

    def __init__(self, tasks: [Task]) -> None:
        self.queue = deque(tasks)
    
    def get_next_task(self) -> Task:
        task = self.queue.popleft()
        self.queue.append(task)
        return task
    
    def add_task_upfront(self, task: Task) -> None:
        self.queue.appendleft(task)
    
    def add_task_back(self, task: Task) -> None:
        self.queue.append(task)