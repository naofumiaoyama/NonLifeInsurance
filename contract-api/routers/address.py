from auth.oauth2 import get_current_user
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal, get_db
import db.models
from fastapi import Depends, APIRouter
from typing import Optional
from routers.schemas import Address
import sys
sys.path.append("..")


router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}}
)


@router.post("/")
async def create_address(address: Address,
                         user: dict = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    # if user is None:
    #     raise get_user_exception()
    address_model = models.Address()
    address_model.id = gen_uuid()
    address_model.postal_code = address.postal_code
    address_model.prefecture_code = address.prefecture_code
    address_model.city_ward_name = address.city_ward_name
    address_model.street = address.street
    address_model.building_name = address.building_name
    address_model.room_number = address.room_number

    db.add(address_model)
    db.flush()
    db.commit()
