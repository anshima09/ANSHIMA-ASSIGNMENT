from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.db.database import engine
from app.User.models import Base
import app.Product.models
import app.Cart.models
import app.Order.models
from app.User.router import router as AuthR
from app.Product.router import router as ProductR
from app.Cart.router import router as CartR
from app.Order.router import router as OrderR
from app.Checkout.router import router as CheckoutR

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers for different modules
app.include_router(CheckoutR, prefix="/order", tags=["checkout"])
app.include_router(OrderR, prefix="/orders", tags=["orders"])
app.include_router(AuthR, prefix="/auth", tags=["users"])
app.include_router(ProductR, prefix="/products", tags=["products"])
app.include_router(CartR, prefix="/cart", tags=["cart"])

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Custom exception handler to return errors in a consistent JSON format.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.detail,
            "code": exc.status_code
        },
    )

@app.get("/")
def root() -> dict:
    """
    Root endpoint for the E-commerce FastAPI Project.
    """
    return {"message": "Welcome to the E-commerce FastAPI Project!"}