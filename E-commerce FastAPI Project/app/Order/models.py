from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base
import enum

# Enum for possible order statuses
class OrderStatusEnum(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"

# Order model representing a customer's order
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)                # Primary key for the order
    user_id = Column(Integer, ForeignKey("users.id"))                 # Foreign key to the user who placed the order
    total_amount = Column(Float)                                      # Total amount for the order
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.paid)  # Status of the order
    created_at = Column(DateTime, default=datetime.utcnow)            # Timestamp when the order was created
    items = relationship("OrderItem", back_populates="order")         # Relationship to order items

# OrderItem model representing an item in an order
class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)                # Primary key for the order item
    order_id = Column(Integer, ForeignKey("orders.id"))               # Foreign key to the order
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)  # Foreign key to the product
    quantity = Column(Integer)                                        # Quantity of the product in the order
    is_deleted = Column(Boolean, default=False)                       # Indicates if the product was soft-deleted (not used directly)
    price_at_purchase = Column(Float)                                 # Price of the product at the time of purchase
    product = relationship("Product")                                 # Relationship to the Product model
    order = relationship("Order", back_populates="items")             # Relationship to the Order model

    @property
    def is_deleted(self):
        # Returns the is_deleted status from the related Product
        return self.product.is_deleted if self.product else False