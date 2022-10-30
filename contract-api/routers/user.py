from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from db.db_user import create_user
from .schemas import User
from db.database import get_db
import sys
sys.path.append("..")

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}}
)


@router.post('/')
def create_user(request: User, db: Session = Depends(get_db)):
    return create_user(db, request)
