class SearchResult:
    def __init__(self, destination_from, destination_to, date_to, date_return, direct, one, two_plus) -> None:
        self.destination_from = destination_from
        self.destination_to = destination_to
        self.date_to = date_to
        self.date_return = date_return
        self.direct = direct
        self.one = one
        self.two_plus = two_plus
    
    def __str__(self) -> str:
        return f'{self.date_to} - {self.date_return} : direct - {self.direct}, one - {self.one}, two and more - {self.two_plus}'
        