import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:s47kaakaa@localhost/TodoApplicationDatabase"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def gen_uuid():
    # For every get request generate uuid
    global uuid_var
    uuid_var = uuid.uuid4()
    return uuid_var
