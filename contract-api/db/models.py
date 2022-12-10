from sqlalchemy import Boolean, Column, Integer, Numeric, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .database import Base


class DbTypeMaster(Base):
    __tablename__ = "type_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    level1_id = Column(Integer)
    group_name_level_1 = Column(String)
    level2_id = Column(Integer)
    group_name_level_2 = Column(String)
    level3_id = Column(Integer)
    group_name_level_3 = Column(String)
    name = Column(String)
    value1 = Column(String)
    value2 = Column(String)
    value3 = Column(String)


class DbCarMaster(Base):
    __tablename__ = "car_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    car_type_id = Column(UUID(as_uuid=True))
    name = Column(String)
    vehicle_model = Column(String)
    car_type = relationship("DbTypeMaster", backref="car_master")


class DbInsuranceMaster(Base):
    __tablename__ = "insurance_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    product_code = Column(String)
    name = Column(String)
    description = Column(String)
    insurance_type_id = Column(UUID(as_uuid=True))
    insurance_type = relationship("DbTypeMaster", backref="insurance_master")


class DbOrganizationMaster(Base):
    __tablename__ = "organization_master"

    id = Column(UUID(as_uuid=True), primary_key=True)
    organization_type_id = Column(UUID(as_uuid=True))
    name = Column(String)
    organization_type = relationship("DbTypeMaster", backref="organization_master")



class DbUser(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class DbAddress(Base):
    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True))
    organization_id = Column(UUID(as_uuid=True))
    postal_code = Column(String)
    prefecture_code = Column(String)
    city_ward_name = Column(String)
    street = Column(String)
    building_name = Column(String)
    room_number = Column(String)

class DbContract(Base):
    __tablename__ = "contracts"

    id = Column(UUID(as_uuid=True), primary_key=True)
    insurance_id = Column(UUID(as_uuid=True))
    poricy_number= Column(String)
    amount = Column(Numeric(5, 3))
    rate = Column(Numeric(5,3))
    premium = Column(Numeric(5,3))
    insurance = relationship("DbInsurances", backref="contracts")
    
class DbInsurances(Base):
    __tablename__ = 'insurances'
    insurance_master_id = Column(UUID(as_uuid=True))
    user_id = Column(UUID(as_uuid=True))
    building_id = Column(UUID(as_uuid=True))
    organization_id = Column(UUID(as_uuid=True))
    car_id = Column(UUID(as_uuid=True))

    insurance_master = relationship("DbInsuranceMaster", backref="insurances")

