from sqlalchemy import Boolean, Column, Decimal, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class CarMaster(Base):
    __tablename__ = "CarMaster"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey(TypeMaster.id))
    name = Column(String)


class TypeMaster(Base):
    __tablename__ = "TypeMaster"

    id = Column(Integer, primary_key=True, index=True)
    type_group = Column(String)
    type_name = Column(String)


class InsuranceMaster(Base):
    __tablename__ = "InsuranceMaster"

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String)
    name = Column(String)
    type_id(Integer, ForeignKey(TypeMaster.id))


class Contracts(Base):
    __tablename__ = "Contracts"

    id = Column(Integer, primary_key=True, index=True)
    insurance_id = Column(Integer, ForeignKey(InsuranceMaster.id))
    policy_number = Column(String)
    amount = Column(Decimal)
    rate = Column(Decimal)
    premium = Column(Decimal)


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="todos")
