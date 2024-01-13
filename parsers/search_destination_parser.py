import json
from models.destination import Destination

def get_destination(destination_json) -> Destination:
    airport = destination_json['data'][0]
    return Destination(airport['skyId'], airport['entityId'])