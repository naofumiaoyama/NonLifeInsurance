import uuid
from pydantic import BaseModel
from datetime import datetime
from typing import List


class TypeMaster(BaseModel):
    group_name_level_1: str
    group_name_level_2: str
    group_name_level_3: str
    name: str
    value1: str
    value2: str
    value3: str


class OrganizationMaster(BaseModel):
    insurance_type: TypeMaster
    name: str


class User(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    is_active: bool


class Address(BaseModel):
    postal_code: str
    prefecture_code: str
    city_ward_name: str
    street: str
    building_name: str
    room_number: str

