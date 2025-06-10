from fastapi import APIRouter

router = APIRouter()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.utils.oauth2 import decode_token
from app.Order.models import Order
from app.Order.schemas import OrderOut, OrderMetaOut

from typing import List

router = APIRouter()


@router.get("/view-orders", response_model=List[OrderMetaOut])
def get_order_history(db: Session = Depends(get_db), user = Depends(decode_token)):
    orders = db.query(Order).filter(Order.user_id == user.id).order_by(Order.created_at.desc()).all()
    return orders

@router.get("/view-orders-by-id/{order_id}", response_model=OrderOut)
def get_order_detail(order_id: int, db: Session = Depends(get_db), user = Depends(decode_token)):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order