import uuid
from auth.oauth2 import get_current_user
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal,get_db
import db.models
from fastapi import Depends, APIRouter
from typing import Optional
from routers.schemas import OrganizationMaster
import sys
sys.path.append("..")


router = APIRouter(
    prefix="/organization_master",
    tags=["organization_master"],
    responses={404: {"description": "Not found"}}
)

@router.post("/")
async def create_organization_master(organization_master: OrganizationMaster,
                                     user: dict = Depends(get_current_user),
                                     db: Session = Depends(get_db)):
    """ if user is None:
        raise get_user_exception() """
    organization_master_model = models.OrganizationMaster()
    organization_master_model.id = gen_uuid()
    organization_master_model.name = organization_master.name
    organization_master_model.insurance_type_id = organization_master.insurance_type_id

    db.add(organization_master_model)
    db.flush()
    db.commit()
