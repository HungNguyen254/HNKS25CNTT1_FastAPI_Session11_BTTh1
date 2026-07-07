from Model import ParkingModel
from Schema import Parking_create,Parking_respones
from sqlalchemy.orm import Session
def create_Parking(parking : Parking_create,database : Session):
    check = database.query(ParkingModel).filter(ParkingModel.slot_code == parking.slot_code).first()
    if check:
        return None
    new_parking = ParkingModel(
        slot_code = parking.slot_code,
        zone_name = parking.zone_name,
        max_weight = parking.max_weight
    )
    database.add(new_parking)
    database.commit()
    database.refresh(new_parking)
    return new_parking
def Show_all_parking(db:Session):
    list_parking = Parking_respones(db)
    return list_parking