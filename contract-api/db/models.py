from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .database import Base


class DbTypeMaster(Base):
    __tablename__ = "type_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    group_name_level_1 = Column(String)
    group_name_level_2 = Column(String)
    group_name_level_3 = Column(String)
    name = Column(String)
    value1 = Column(String)
    value2 = Column(String)
    value3 = Column(String)


"""
class CarMaster(Base):
    __tablename__ = "car_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    type_id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    hehicle_model = Column(String)

    car_type = relationship("TypeMaster", backref="car_master")

class InsuranceMaster(Base):
    __tablename__ = "insurance_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    product_code = Column(String)
    name = Column(String)
    insurance_type_id = Column(UUID(), primary_key=True,)

    insurance_type = relationship("TypeMaster", backref="insurance_master")
 """


class DbUser(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class DbOrganizationMaster(Base):
    __tablename__ = "organization_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
   # insurance_type_id = Column(UUID(as_uuid=True), primary_key=True)


class DbAddress(Base):
    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True)
    #organization_id = Column(UUID(as_uuid=False), primary_key=True)
    postal_code = Column(String)
    prefecture_code = Column(String)
    city_ward_name = Column(String)
    street = Column(String)
    building_name = Column(String)
    room_number = Column(String)
