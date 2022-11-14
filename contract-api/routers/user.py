from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from db.db_user import create_new_user, get_user_by_username, get_all
from .schemas import User
from db.database import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get('')
async def all_users(db: Session = Depends(get_db)):
    return await get_all(db)


@router.post('/')
async def create_user(user: User, db: Session = Depends(get_db)):
    await create_new_user(user, db)


@router.get('/username')
def get_user(username: str, db: Session = Depends(get_db)):
    return get_user_by_username(username, db)
