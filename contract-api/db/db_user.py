from fastapi import HTTPException, status, Depends
from .models import DbUser
from routers.schemas import User
from sqlalchemy.orm.session import Session
from .hashing import Hash
from .database import gen_uuid, get_db

async def create_new_user(user: User, db):
    new_user = DbUser(
        id=gen_uuid(),
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=Hash.bcrypt(user.password),
        is_active=user.is_active
    )
    db.add(new_user)
    db.flush()
    db.commit()


async def get_all(db):
    users = db.query(DbUser).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'db not found')
    return users


async def get_user_by_username(username: str, db):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return user
