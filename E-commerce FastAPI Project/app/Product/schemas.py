from pydantic import BaseModel, Field
from typing import Optional

# Base schema for product (shared fields)
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="Price must be greater than 0")  # Product price, must be > 0
    stock: int  # Available stock
    category: Optional[str] = None  # Product category
    image_url: Optional[str] = None  # URL to product image
    

# Schema for creating a new product (inherits from ProductBase)
class ProductCreate(ProductBase):
    pass

# Schema for updating an existing product (all fields optional)
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[str] = None
    image_url: Optional[str] = None

# Schema for product output/response (includes id and is_deleted fields)
class ProductOut(ProductBase):
    id: int  # Product ID
    is_deleted: bool  # Indicates if the product is soft-deleted

    class Config:
        from_attributes = True  # Enable ORM mode