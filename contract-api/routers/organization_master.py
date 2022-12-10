from auth.oauth2 import get_current_user
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal, get_db
from db.db_organization_master import create_new_organization_master, remove_organization_master_byId, get_all
from fastapi import Depends, APIRouter
from typing import Optional
from routers.schemas import OrganizationMaster

router = APIRouter(
    prefix="/organization_master",
    tags=["organization_master"],
)

@router.get('')
async def all_oraganization_masters(db: Session = Depends(get_db)):
    return await get_all(db)


@router.post("/")
async def create_organization_master(organization_master: OrganizationMaster, db: Session = Depends(get_db)):
    await create_new_organization_master(organization_master, db)


@router.delete("/")
async def remove_organization_master(organization_master: OrganizationMaster, db: Session = Depends(get_db)):
    await remove_organization_master_byId(organization_master, db)
