from fastapi import APIRouter, Depends, HTTPException
from app.Cart.models import CartItem
from app.Cart.schemas import CartItemCreate,CartItemOut,CartItemUpdate,CartItemBase
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.User.models import User
from app.Product.models import Product
from typing import List
from app.utils.oauth2 import decode_token

router = APIRouter()

@router.post("/addToCart")
def add_cart_item(item: CartItemCreate, db: Session = Depends(get_db), user: User = Depends(decode_token)):
    db_item = CartItem(**item.dict(), user_id=user.id)
    if not db_item.product_id:
        raise HTTPException(status_code=400, detail="Product with this ID does not exist.")
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item added to cart", "item": db_item}


@router.get("/viewCart", response_model=List[CartItemOut])
def view_cart(db: Session = Depends(get_db), user: User = Depends(decode_token)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user.id).all()
    if not cart_items:
        raise HTTPException(status_code=404, detail="Cart is empty")
    return cart_items

@router.put("/update-cart/{item_id}", response_model=CartItemOut)
def update_cart_item(item_id: int, item: CartItemUpdate, db: Session = Depends(get_db), user: User = Depends(decode_token)):
    db_item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == user.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/delete-cart/{item_id}", response_model=str)
def delete_cart_item(item_id: int, db: Session = Depends(get_db), user: User = Depends(decode_token)):
    db_item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == user.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    
    db.delete(db_item)
    db.commit()
    return "Item deleted from cart"