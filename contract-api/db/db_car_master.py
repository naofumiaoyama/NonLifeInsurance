from fastapi import HTTPException, status
from .models import DbCarMaster
from routers.schemas import CarMaster
from sqlalchemy.orm.session import Session
from .database import gen_uuid
from sqlalchemy.dialects.postgresql import UUID
async def get_all(db):
    carMasters = db.query(DbCarMaster).all()    
    if not carMasters:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username not found')
    return carMasters

async def create_new_car_master(car_master: CarMaster, db: Session):
    new_car_master = DbCarMaster(
        id=gen_uuid(),
        name=car_master.name,
        car_type_id=UUID(car_master.car_type_id),
        vehicle_model=car_master.vehicle_model
    )
    db.add(new_car_master)
    db.flush()
    db.commit()

async def remove_car_master_byId(car_master: CarMaster, db: Session):
    found_car_master = db.query(DbCarMaster).filter_by(id=car_master.id).first()
    db.delete(found_car_master)
    db.flush()
    db.commit()

async def get_car_master_by_name(db: Session, name: str):
    car_master = db.query(DbCarMaster).filter(
        DbCarMaster.name == name).first()
    if not car_master:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'CarMaster with name not found')
    return car_master
