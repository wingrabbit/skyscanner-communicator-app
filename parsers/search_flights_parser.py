import json

def get_prices(flight_json):
    return flight_json['data']['filterStats']['stopPrices']