from fastapi import FastAPI
from app.db.database import engine
from app.models.users import Base
from app.routers import Authr, Userr




Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(Userr.router, prefix="/users", tags=["users"])
app.include_router(Authr.router, prefix="/users", tags=["auth"])


@app.get("/")
def root():
    return {"message" : "Welcome to the E-commerce FastAPI Project!"}




