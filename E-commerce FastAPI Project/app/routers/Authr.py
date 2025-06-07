from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usersS import UserLogin
from app.models.users import User
from app.utils.utils import verify_password

router = APIRouter()

@router.post("/login")
def login(users_credentials: UserLogin, db:Session = Depends(get_db)):
    user= db.query(User).filter(User.email == users_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not verify_password(users_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    return {"Token" : "Your JWT Token here"}


