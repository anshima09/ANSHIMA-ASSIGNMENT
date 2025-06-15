from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.Product import models
from app.User import models

# CartItem model representing an item in a user's shopping cart
class CartItem(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)                # Primary key for the cart item
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Foreign key to the user who owns the cart
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False) # Foreign key to the product in the cart
    quantity = Column(Integer, nullable=False)                        # Quantity of the product in the cart

    # Relationships
    user = relationship("User", back_populates="cart_items")          # Relationship to the User model
    product = relationship("Product", back_populates="cart_items")    # Relationship to the Product