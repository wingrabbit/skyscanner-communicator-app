import requests
from config import X_RapidAPI_Key, X_RapidAPI_Host, API_URL

class GeneralQuery:
    url = API_URL
    
    query_string = {}
    
    headers = {
        "X-RapidAPI-Key": X_RapidAPI_Key,
        "X-RapidAPI-Host": X_RapidAPI_Host
    }

    def __init__(self) -> None:
        pass

    def execute(self) -> str:
        return requests.get(self.url, headers=self.headers, params=self.query_string).json()

