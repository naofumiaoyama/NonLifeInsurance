from fastapi import HTTPException, status
from .models import DbUsers
from routers.schemas import User
from sqlalchemy.orm.session import Session
from .hashing import Hash
from .database import gen_uuid


def create_user(db: Session, request: User):
    new_user = DbUser(
        id=gen_uuid(),
        email=request.email,
        username=request.username,
        first_name=request.first_name,
        last_name=request.last_name,
        hashed_password=Hash.bcrypt(request.password),
        is_active=request.is_active
    )
    db.add(new_user)
    db.flush()
    db.commit()

    return new_user


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUsers).filter(DbUsers.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return user
