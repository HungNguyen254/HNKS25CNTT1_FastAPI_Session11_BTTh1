from pydantic import BaseModel
class Parking_create(BaseModel):
    slot_code : str
    zone_name : str
    max_weight: int
class Parking_respones(BaseModel):
    id : int
    slot_code : str
    zone_name : str
    max_weight: int
    is_available : bool
    
    class config():
        from_attributes = True