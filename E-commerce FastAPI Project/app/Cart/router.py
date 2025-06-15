from fastapi import APIRouter, Depends, HTTPException
from app.Cart.models import CartItem
from app.Cart.schemas import CartItemCreate, CartItemOut, CartItemUpdate, CartItemBase, AddToCartResponse
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.User.models import User
from app.Product.models import Product
from typing import List, Dict, Any
from app.utils.oauth2 import decode_token
from app.db.config import logger

router = APIRouter()

# Endpoint to add an item to the user's cart
@router.post("/addToCart",response_model=AddToCartResponse)
def add_cart_item(
    item: CartItemCreate,
    db: Session = Depends(get_db),
    user: User = Depends(decode_token)
) -> Dict[str, Any]:
    """
    Add an item to the user's cart.
    Checks if the product exists and is not deleted before adding.
    """
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if not product:
        logger.warning(f"User {user.id} tried to add a cart item with missing product_id {item.product_id}.")
        raise HTTPException(status_code=400, detail="Product with this ID does not exist.")
    if product.is_deleted:
        logger.warning(f"User {user.id} tried to add deleted product {item.product_id} to cart.")
        raise HTTPException(status_code=400, detail="Cannot add deleted product to cart.")

    db_item = CartItem(**item.dict(), user_id=user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    logger.info(f"User {user.id} added product {db_item.product_id} (qty: {db_item.quantity}) to cart.")
    return {
        "message": "Item added to cart",
        "item": db_item
    }

# Endpoint to view all items in the user's cart
@router.get("/viewCart", response_model=List[CartItemOut])
def view_cart(
    db: Session = Depends(get_db),
    user: User = Depends(decode_token)
) -> List[CartItemOut]:
    """
    View all items in the user's cart.
    """
    cart_items = db.query(CartItem).filter(CartItem.user_id == user.id).all()
    if not cart_items:
        logger.warning(f"User {user.id} viewed cart but it is empty.")
        raise HTTPException(status_code=404, detail="Cart is empty")
    logger.info(f"User {user.id} viewed their cart. Items: {len(cart_items)}")
    return cart_items

# Endpoint to update the quantity or details of a specific cart item
@router.put("/update-cart/{item_id}", response_model=AddToCartResponse)
def update_cart_item(
    item_id: int,
    item: CartItemUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(decode_token)
) -> CartItemOut:
    """
    Update the quantity or details of a specific cart item.
    """
    db_item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == user.id).first()
    if not db_item:
        logger.warning(f"User {user.id} tried to update non-existent cart item {item_id}.")
        raise HTTPException(status_code=404, detail="Item not found in cart")
    
    product = db.query(Product).filter(Product.id == db_item.product_id).first()
    if not product or product.is_deleted:
        logger.warning(f"User {user.id} tried to update cart item {item_id} with deleted product {db_item.product_id}.")
        raise HTTPException(status_code=400, detail="Cannot update cart item for a deleted product.")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    logger.info(f"User {user.id} updated cart item {item_id}.")
    return {
        "message": "Item quantity updated",
        "item": db_item
    }

# Endpoint to delete a specific item from the user's cart
@router.delete("/delete-cart/{item_id}", response_model=str)
def delete_cart_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(decode_token)
) -> str:
    """
    Delete a specific item from the user's cart.
    """
    db_item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == user.id).first()
    if not db_item:
        logger.warning(f"User {user.id} tried to delete non-existent cart item {item_id}.")
        raise HTTPException(status_code=404, detail="Item not found in cart")
    db.delete(db_item)
    db.commit()
    logger.info(f"User {user.id} deleted cart item {item_id}.")
    return "Item deleted from cart with ID: "+ str(item_id)