from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.utils.oauth2 import decode_token
from app.Order.models import Order
from app.Order.schemas import OrderOut, OrderMetaOut
from app.db.config import logger
from typing import List

router = APIRouter()

# Endpoint to retrieve the order history for the currently authenticated user

@router.get("/view-orders", response_model=List[OrderMetaOut])
def get_order_history(
    db: Session = Depends(get_db),
    user = Depends(decode_token)
) -> List[OrderMetaOut]:
    """
    Retrieve the order history for the currently authenticated user.
    Returns a list of order metadata.
    """
    orders = db.query(Order).filter(Order.user_id == user.id).order_by(Order.created_at.desc()).all()
    if not orders:
        logger.warning(f"User {user.id} has no orders in history.")
        raise HTTPException(status_code=404, detail="No orders found.")
    logger.info(f"User {user.id} fetched their order history. Total orders: {len(orders)}")
    return orders

# Endpoint to retrieve the details of a specific order by order ID for the authenticated user
@router.get("/view-orders-by-id/{order_id}", response_model=OrderOut)
def get_order_detail(
    order_id: int,
    db: Session = Depends(get_db),
    user = Depends(decode_token)
) -> OrderOut:
    """
    Retrieve the details of a specific order by order ID for the authenticated user.
    Returns the order details including line items.
    """
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == user.id).first()
    if not order:
        logger.warning(f"User {user.id} tried to fetch non-existent or unauthorized order ID {order_id}")
        raise HTTPException(status_code=404, detail="Order not found")
    logger.info(f"User {user.id} fetched details for order ID {order_id}")
    return order