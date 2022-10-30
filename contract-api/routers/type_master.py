import uuid
from auth.oauth2 import get_current_user
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal, get_db, gen_uuid
from db.models import DbTypeMaster
from fastapi import Depends, APIRouter
from typing import Optional
from routers.schemas import TypeMaster
import sys
sys.path.append("..")


router = APIRouter(
    prefix="/type_master",
    tags=["type_master"],
    responses={404: {"description": "Not found"}}
)


@router.post("/")
async def create_type_master(type_master: TypeMaster,
                             user: dict = Depends(get_current_user),
                             db: Session = Depends(get_db)):
    """ if user is None:
        raise get_user_exception() """
    type_master_model = DbTypeMaster()
    type_master_model.id = gen_uuid()
    type_master_model.group_name_level_1 = type_master.group_name_level_1
    type_master_model.group_name_level_2 = type_master.group_name_level_2
    type_master_model.group_name_level_3 = type_master.group_name_level_3
    type_master_model.name = type_master.name
    type_master_model.value1 = type_master.value1
    type_master_model.value2 = type_master.value2
    type_master_model.value3 = type_master.value3

    db.add(type_master_model)
    db.flush()
    db.commit()
