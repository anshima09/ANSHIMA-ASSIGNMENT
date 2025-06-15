from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from app.db.database import Base
import enum
from sqlalchemy.orm import relationship

# Enum for user roles (admin or user)
class UserRole(str, enum.Enum):
    admin = "admin"
    user = "user"

# User model representing application users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the user
    name = Column(String, nullable=False)               # User's name (required)
    email = Column(String, unique=True, index=True, nullable=False)  # Unique email (required)
    password = Column(String, nullable=False)           # Hashed password (required)
    role = Column(Enum(UserRole), default=UserRole.user)  # User role, defaults to 'user'
    cart_items = relationship(
        "CartItem", back_populates="user", cascade="all, delete-orphan"
    )  # Relationship to CartItem (user's cart items)
    products = relationship(
        "Product", back_populates="creator", cascade="all, delete"
    )  # Relationship to Product (products created by user)

# Model for password reset tokens
class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the token
    token = Column(String, unique=True, nullable=False, index=True)  # Unique reset token string
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to User
    expires_at = Column(DateTime, nullable=False)  # Expiry datetime for the token

    user = relationship("User")  # Relationship to the User