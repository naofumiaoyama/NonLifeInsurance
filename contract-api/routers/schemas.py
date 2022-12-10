from pydantic import BaseModel
from datetime import datetime
from typing import List

class TypeMaster(BaseModel):
    id: str
    group_name_level_1: str
    group_name_level_2: str
    group_name_level_3: str
    name: str
    value1: str
    value2: str
    value3: str


class OrganizationMaster(BaseModel):
    id: str
    name: str


class CarMaster(BaseModel):
    id: str
    name: str    
    car_type_id: str
    vehicle_model: str


class User(BaseModel):
    id: str
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    is_active: bool


class Address(BaseModel):
    id: str
    postal_code: str
    prefecture_code: str
    city_ward_name: str
    street: str
    building_name: str
    room_number: str
