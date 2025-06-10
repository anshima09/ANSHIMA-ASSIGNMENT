from pydantic import BaseModel


class CartItemBase(BaseModel):
    product_id: int
    quantity: int


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    quantity: int


class CartItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True

