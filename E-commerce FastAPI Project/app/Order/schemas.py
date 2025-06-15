from pydantic import BaseModel
from typing import List
from datetime import datetime

# Schema for a single order item in an order
class OrderItemOut(BaseModel):
    id: int                        # Order item ID
    product_id: int                # Associated product ID
    quantity: int                  # Quantity of the product in the order
    price_at_purchase: float       # Price of the product at the time of purchase
    is_deleted: bool               # Indicates if the product was soft-deleted

    class Config:
        from_attributes = True     # Enable ORM mode for SQLAlchemy models

# Schema for an order with its items
class OrderOut(BaseModel):
    id: int                        # Order ID
    user_id: int                   # User who placed the order
    total_amount: float            # Total order amount
    status: str                    # Order status (e.g., paid, pending)
    created_at: datetime           # Timestamp when the order was created
    items: List[OrderItemOut]      # List of order items

    class Config:
        from_attributes = True     # Enable ORM mode for SQLAlchemy models

# Schema for order metadata (without items)
class OrderMetaOut(BaseModel):
    id: int                        # Order ID
    user_id: int                   # User who placed the order
    total_amount: float            # Total order amount
    status: str                    # Order status
    created_at: datetime           # Timestamp when the order was created

    class Config:
        from_attributes = True     # Enable ORM mode for

        