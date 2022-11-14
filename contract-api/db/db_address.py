from fastapi import HTTPException, status
from .models import DbAddress
from routers.schemas import Address
from sqlalchemy.orm.session import Session
from .database import gen_uuid


async def create_new_address(address: Address, db):
    address_model = DbAddress(
        id=gen_uuid(),
        postal_code=address.postal_code,
        prefecture_code=address.prefecture_code,
        city_ward_name=address.city_ward_name,
        street=address.street,
        building_name=address.building_name,
        room_number=address.room_number
    )

    db.add(address_model)
    db.flush()
    db.commit()


async def get_all(db):
    addresses = db.query(DbAddress).all()
    if not addresses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return addresses
