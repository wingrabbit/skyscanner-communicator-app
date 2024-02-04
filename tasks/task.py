from models.destination import Destination

class Task:
    def __init__(self, origin: Destination, destination: Destination, date_to, date_return, id=None, search_id=None) -> None:
        self.origin = origin
        self.destination = destination
        self.date_to = date_to
        self.date_return = date_return
        self.id = id
        self.search_id = search_id
    
    def __str__(self) -> str:
        return str(self.id) + ' ' + str(self.search_id) + ' ' + str(self.origin) + ' ' + str(self.destination) + ' ' + str(self.date_to) + ' ' + str(self.date_return)