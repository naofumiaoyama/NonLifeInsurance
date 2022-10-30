from os import name
from fastapi import FastAPI
from db import models
from db.database import engine
from auth import authentication
from routers import user, address, type_master, organization_master
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(address.router)
app.include_router(type_master.router)
app.include_router(organization_master.router)
app.include_router(authentication.router)

origins = [
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:3002'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)
