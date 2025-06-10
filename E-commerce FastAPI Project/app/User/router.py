from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.User.models import User
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.User.schemas import UserSignup, UserOut,ForgotPassword, ResetPassword
from app.User.models import User,PasswordResetToken
from sqlalchemy.orm import Session
from typing import List
from app.utils.utils import hash_password, generate_reset_token, verify_password
from datetime import datetime
from app.utils import oauth2


router = APIRouter()

@router.post("/signin")
def login(users_credentials: OAuth2PasswordRequestForm=Depends(), db:Session = Depends(get_db)):
    user= db.query(User).filter(User.email == users_credentials.username).first()
    
    if not user or not verify_password(users_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    token_data = {"user_id": user.id, "role": user.role}
    return {
        "access_token": oauth2.create_access_token(token_data),
        "refresh_token": oauth2.create_refresh_token(token_data),
        "token_type": "bearer",
        "user": user.email
    }


@router.post("/signup", status_code=status.HTTP_201_CREATED,response_model=UserOut)
def signup(user: UserSignup,db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user_data = user.dict()
    user_data["password"] = hash_password(user_data["password"])
    print(user_data)
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#admin sepcific
@router.get("/getAllUsers", response_model=List[UserOut])
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found!")
    return users



@router.post("/forgot-password",status_code=status.HTTP_201_CREATED)
def secure_forgot_password(request: ForgotPassword, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    token, expires_at = generate_reset_token()
    reset_token = PasswordResetToken(token=token, user_id=user.id, expires_at=expires_at)
    db.add(reset_token)
    db.commit()
    
    return {"message": "Reset token created", "token": token}  


@router.post("/reset-password")
def secure_reset_password(request: ResetPassword, db: Session = Depends(get_db)):
    token_entry = db.query(PasswordResetToken).filter(PasswordResetToken.token == request.token).first()

    if not token_entry or token_entry.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired token.")

    user = db.query(User).filter(User.id == token_entry.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    user.password = hash_password(request.new_password)

    # Invalidate token after use
    db.delete(token_entry)
    db.commit()

    return {"message": "Password successfully reset"}


