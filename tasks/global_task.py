class GlobalTask:
    
    def __init__(self, origin: str, destination: str, dates_range: list[str], days_range: list[int]) -> None:
        self.origin = origin
        self.destination = destination
        self.dates_range = dates_range
        self.days_range = days_range