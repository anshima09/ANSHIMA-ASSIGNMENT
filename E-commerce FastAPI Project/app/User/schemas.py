from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from typing import Optional

# Enum for user roles
class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

# Schema for user signup request
class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.user  # Default role is 'user'

# Schema for user login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for user output/response
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: RoleEnum

    class Config:
        from_attributes = True  # Enable ORM mode for SQLAlchemy models

# Schema for JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema for token data (used in authentication)
class TokenData(BaseModel):
    id: Optional[str]=None

# Schema for forgot password request
class ForgotPassword(BaseModel):
    email: EmailStr

# Schema for reset password request
class ResetPassword(BaseModel):
    token: str
    new_password: str = Field(..., min_length=6)  # Password must be at least 6 characters