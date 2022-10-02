from .auth import get_current_user, get_user_exception
from pydantic import BaseModel, Field
from sqlalchemy.orm import Sesstion
from database import engine, SessionLocal
import models
from fastapi import Depends, HTTPException, APIRouter
from typing import Optional
import sys
sys.path.append("..")


router = APIRouter(
    prefix="/cars",
    tags=["cars"],
    resposes={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class CarMaster(BaseModel):
    id: int
    type_id: int 
    name: str
    
    
