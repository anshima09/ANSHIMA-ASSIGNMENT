from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.usersS import UserLogin
from app.models.users import User
from app.utils.utils import verify_password
from app.utils import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter()

@router.post("/login")
def login(users_credentials: OAuth2PasswordRequestForm=Depends(), db:Session = Depends(get_db)):
    user= db.query(User).filter(User.email == users_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not verify_password(users_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data= {"user_id": user.id})
    return {"access_token" : access_token, "token_type": "bearer"}


