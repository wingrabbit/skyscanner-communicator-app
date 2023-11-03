class Destination:
    def __init__(self, sky_id, entity_id, entity_type=None, title=None) -> None:
        self.sky_id = sky_id
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.title = title