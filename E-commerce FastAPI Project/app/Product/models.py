from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.Order.models import OrderItem
from app.Cart.models import CartItem

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    category = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    is_deleted = Column(Boolean,default=False,nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)   

    cart_items = relationship("CartItem", back_populates="product", cascade="all, delete-orphan")
    order_items = relationship("OrderItem", back_populates="product")
    creator = relationship("User", back_populates="products")

