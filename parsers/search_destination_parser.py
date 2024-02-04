import json
from models.destination import Destination

def get_destination(destination_json) -> Destination:
    airport = destination_json['data'][0]
    return Destination(sky_id=airport['skyId'], entity_id=airport['entityId'], title=airport['presentation']['title'])