from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


# Product model representing products in the e-commerce platform
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the product
    name = Column(String, nullable=False)               # Product name (required)
    description = Column(String, nullable=True)         # Product description (optional)
    price = Column(Float, nullable=False)               # Product price (required)
    stock = Column(Integer, default=0)                  # Available stock (default 0)
    category = Column(String, nullable=True)            # Product category (optional)
    image_url = Column(String, nullable=True)           # URL to product image (optional)
    is_deleted = Column(Boolean, default=False, nullable=False)  # Soft delete flag
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to creator (User)

    # Relationship to CartItem (products in users' carts)
    cart_items = relationship("CartItem", back_populates="product", cascade="all, delete-orphan")
    # Relationship to OrderItem (products in orders)
    order_items = relationship("OrderItem", back_populates="product")
    # Relationship to User who created the product
    creator = relationship("User", back_populates="products")