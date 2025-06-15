from pydantic import BaseModel

# Base schema for cart item (shared fields)
class CartItemBase(BaseModel):
    product_id: int  # ID of the product to add to cart
    quantity: int    # Quantity of the product

# Schema for creating a new cart item (inherits from CartItemBase)
class CartItemCreate(CartItemBase):
    pass

# Schema for updating the quantity of a cart item
class CartItemUpdate(BaseModel):
    quantity: int  # New quantity for the cart item

# Schema for cart item output/response
class CartItemOut(BaseModel):
    id: int           # Cart item ID
    product_id: int   # Associated product ID
    quantity: int     # Quantity of the product in the cart

    class Config:
        from_attributes = True  # Enable ORM mode for SQLAlchemy models

# Schema for the response after adding an item to the cart
class AddToCartResponse(BaseModel):
    message: str         # Success message
    item: CartItemOut    # The cart item that was