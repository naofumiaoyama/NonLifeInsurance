from auth.oauth2 import get_current_user
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal, get_db
from db.db_car_master import create_new_car_master, remove_car_master_byId, get_all
from fastapi import Depends, APIRouter
from typing import Optional
from routers.schemas import CarMaster

router = APIRouter(
    prefix="/car_master",
    tags=["car_master"],
)

@router.get('')
async def all_oraganization_masters(db: Session = Depends(get_db)):
    return await get_all(db)


@router.post("/")
async def create_car_master(car_master: CarMaster, db: Session = Depends(get_db)):
    await create_new_car_master(car_master, db)


@router.delete("/")
async def remove_car_master(car_master: CarMaster, db: Session = Depends(get_db)):
    await remove_car_master_byId(car_master, db)
