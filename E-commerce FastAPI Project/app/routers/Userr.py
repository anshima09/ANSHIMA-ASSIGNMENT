from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from app.schemas.usersS import UserSignup, UserOut
from sqlalchemy.orm import Session
from app.db.database import engine, get_db
from app.models.users import Base,User
from app.utils.utils import hash_password
from typing import List

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED,response_model=UserOut)
def signup(user: UserSignup,db: Session = Depends(get_db)):
    user_data = user.dict()
    user_data["password"] = hash_password(user_data["password"])
    print(user_data)
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/getUsersById/{id}",response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found!")
    return user

@router.get("/getAllUsers", response_model=List[UserOut])
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found!")
    return users


