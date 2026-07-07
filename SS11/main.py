from fastapi import FastAPI,status,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db,Base,engine
from Schema import *
from Model import *
from Service import *

app = FastAPI()
Base.metadata.create_all(bind=engine)
@app.post('/Parking',status_code=status.HTTP_201_CREATED)
async def create_parking(new_parking: Parking_create,database:Session = Depends(get_db)):
    New_parkings = create_Parking(parking = new_parking,database = database)
    if New_parkings is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Cho do xe da co tu truoc')
    return {'message':'Them cho do xe thanh cong','data':New_parkings}
@app.get('/Parking')
async def show_parking(db:Session = Depends(get_db)):
    list_parking = show_parking(db)
    return list_parking