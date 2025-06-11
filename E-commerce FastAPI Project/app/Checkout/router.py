from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.utils.oauth2 import decode_token
from app.Cart.models import CartItem
from app.Product.models import Product
from app.Order.models import Order, OrderItem
from app.Checkout.schemas import CheckoutResponse
from datetime import datetime
from app.db.config import logger

router = APIRouter()

@router.post("/checkout", response_model=CheckoutResponse)
def checkout(db: Session = Depends(get_db), user = Depends(decode_token)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user.id).all()
    if not cart_items:
        logger.warning(f"User {user.id} attempted checkout with empty cart.")
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_amount = 0
    order_items = []

    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            logger.warning(f"Product ID {item.product_id} not found during checkout for user {user.id}.")
            continue
        item_total = item.quantity * product.price
        total_amount += item_total
        order_items.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "price_at_purchase": product.price
        })

    order = Order(
        user_id=user.id,
        total_amount=total_amount,
        status="paid",
        created_at=datetime.utcnow()
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    logger.info(f"Order {order.id} created for user {user.id} with total {total_amount}.")

    for oi in order_items:
        db.add(OrderItem(order_id=order.id, **oi))
    db.commit()
    logger.info(f"Order items added for order {order.id}.")

    for item in cart_items:
        db.delete(item)
    db.commit()
    logger.info(f"Cart cleared for user {user.id} after checkout.")

    return CheckoutResponse(
        message="Payment successful (dummy)! Order placed.",
        order_id=order.id,
        total_amount=total_amount
    )