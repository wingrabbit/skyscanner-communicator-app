from models.destination import Destination

class Task:
    def __init__(self, origin: Destination, destination: Destination, date_to, date_return) -> None:
        self.origin = origin
        self.destination = destination
        self.date_to = date_to
        self.date_return = date_return
    
    def __str__(self) -> str:
        return str(self.origin) + ' ' + str(self.destination) + ' ' + str(self.date_to) + ' ' + str(self.date_return)