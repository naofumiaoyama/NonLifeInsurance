from fastapi import HTTPException, status
from db.models import DbOrganizationMaster
from routers.schemas import OrganizationMaster
from sqlalchemy.orm.session import Session
from .database import gen_uuid


def create_organization_master(db: Session, request: OrganizationMaster):
    new_organization_master = DbOrganizationMaster(
        id=gen_uuid(),
        name=request.name,
        insurance_type_id=request.insurance_type_id
    )
    db.add(new_organization_master)
    db.flush()
    db.commit()
    return new_organization_master


def get_organization_master_by_name(db: Session, name: str):
    organization_master = db.query(DbOrganizationMaster).filter(
        DbOrganizationMaster.name == name).first()
    if not organization_master:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'OrganizationMaster with name {name} not found')
    return organization_master
