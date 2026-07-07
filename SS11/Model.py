from database import Base
from sqlalchemy import Column,String,Integer,Boolean
class ParkingModel(Base):
    __tablename__ = 'Parkings'
    id = Column(Integer,primary_key=True,autoincrement=True)
    slot_code = Column(String(50),nullable=False,unique=True)
    zone_name = Column(String(50),nullable=False)
    max_weight = Column(Integer,nullable=False)
    is_available = Column(Boolean,default=1)