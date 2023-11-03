class Task:
    def __init__(self, origin, destination, date_to, date_return) -> None:
        self.origin = origin
        self.destination = destination
        self.date_to = date_to
        self.date_return = date_return
    
    def __str__(self) -> str:
        return self.origin + ' ' + self.destination + ' ' + str(self.date_to) + ' ' + str(self.date_return)