from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base
import enum

class OrderStatusEnum(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Float)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.paid)
    created_at = Column(DateTime, default=datetime.utcnow)
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)  
    quantity = Column(Integer)
    is_deleted = Column(Boolean, default=False)
    price_at_purchase = Column(Float)
    product = relationship("Product")
    order = relationship("Order", back_populates="items")

    @property
    def is_deleted(self):
        return self.product.is_deleted if self.product else False