from fastapi import HTTPException, status
from .models import DbOrganizationMaster
from routers.schemas import OrganizationMaster
from sqlalchemy.orm.session import Session
from .database import gen_uuid


async def get_all(db):
    organizationMasters = db.query(DbOrganizationMaster).all()    
    if not organizationMasters:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username not found')
    return organizationMasters


async def create_new_organizaton_master(organization_master: OrganizationMaster, db: Session):
    new_organization_master = DbOrganizationMaster(
        id=gen_uuid(),
        name=organization_master.name
    )
    db.add(new_organization_master)
    db.flush()
    db.commit()


def get_organization_master_by_name(db: Session, name: str):
    organization_master = db.query(DbOrganizationMaster).filter(
        DbOrganizationMaster.name == name).first()
    if not organization_master:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'OrganizationMaster with name not found')
    return organization_master
