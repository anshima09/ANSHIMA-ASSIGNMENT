from fastapi import FastAPI
from app.db.database import engine
from app.User.models import Base
import app.Product.models 
import app.Cart.models
from app.User.router import router as AuthR
from app.Product.router import router as ProductR
from app.Cart.router import router as CartR


Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(AuthR, prefix="/auth", tags=["users"])
app.include_router(ProductR, prefix="/products", tags=["products"])
app.include_router(CartR, prefix="/cart", tags=["cart"])


@app.get("/")
def root():
    return {"message" : "Welcome to the E-commerce FastAPI Project!"}




