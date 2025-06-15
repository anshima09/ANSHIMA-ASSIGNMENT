from pydantic import BaseModel,Field
from typing import Optional


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="Price must be greater than 0")    
    stock: int
    category: Optional[str] = None
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    
class ProductOut(ProductBase):
    
    id: int
    is_deleted: bool
    

    class Config:
        from_attributes = True

