from auth.oauth2 import get_current_user
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal, get_db
import db.models
from db.db_address import create_new_address, get_all
from fastapi import Depends, APIRouter
from typing import Optional
from .schemas import Address
import sys
sys.path.append("..")


router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}}
)


@router.get('')
async def all_addresses(db: Session = Depends(get_db)):
    return await get_all(db)


@router.post("/")
async def create_address(address: Address,
                         user: dict = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    # if user is None:
    #     raise get_user_exception()

    await create_new_address(address, db=db)
