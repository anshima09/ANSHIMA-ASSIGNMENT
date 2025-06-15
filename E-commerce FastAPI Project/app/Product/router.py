from fastapi import APIRouter, Depends, HTTPException, status,Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.Product.models import Product
from app.Product.schemas import ProductCreate,ProductOut
from app.utils.oauth2 import decode_token
from typing import List
from sqlalchemy import or_
from app.db.config import logger
from typing import List, Dict


router = APIRouter()

def admin_required(user):
    """
    Utility function to check if the user is an admin.
    Raises HTTPException if not.
    """
    if not hasattr(user, "role") or user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required.")
    return True

# admin can create a product
@router.post("/create-product", status_code=status.HTTP_201_CREATED, response_model=ProductOut)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    user= Depends(decode_token)
) -> ProductOut:
    """
    Admin endpoint to create a new product.
    """
    admin_required(user)
    new_product = Product(**product.dict(),created_by=user.id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    logger.info(f"Product created: {new_product.name} by admin {user.id}")
    return new_product


#admin can get all products
@router.get("/getAllProducts", response_model=List[ProductOut])
def get_all_products(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1, le=100), 
    db: Session = Depends(get_db),
    user= Depends(decode_token)
) -> List[ProductOut]:
    """
    Admin endpoint to retrieve all products with pagination.
    """
    admin_required(user)
    products = db.query(Product).filter(Product.is_deleted == False).offset(skip).limit(limit).all()
    if not products:
        logger.warning("No products found in the database (admin endpoint).")
        raise HTTPException(status_code=404, detail="No products found.")
    logger.info(f"Admin {user.id} fetched all products. Total: {len(products)}")
    return products


#admin can get product by id
@router.get("/getProductById/{product_id}", response_model=ProductOut)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
    user = Depends(decode_token)
) -> ProductOut:
    """
    Admin endpoint to get a product by its ID.
    """
    admin_required(user)
    product = db.query(Product).filter(Product.id == product_id,Product.is_deleted == False).first()
    if not product:
        logger.warning(f"Admin {user.get('user_id')} tried to fetch non-existent product ID {product_id}")
        raise HTTPException(status_code=404, detail="Product not found.")
    logger.info(f"Admin {user.id} fetched product ID {product_id}")
    return product

#admin can update product details 
@router.put("/update-product/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
    user = Depends(decode_token)
) -> ProductOut:
    """
    Admin endpoint to update product details.
    """
    
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        logger.warning(f"Admin {user.id} tried to update non-existent product ID {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    if existing_product.created_by != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to modify this product.")
    # Update fields
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.stock = product.stock
    existing_product.category = product.category
    existing_product.image_url = product.image_url
    db.commit()
    db.refresh(existing_product)
    logger.info(f"Product ID {product_id} updated by admin {user.id}")
    return existing_product

#admin can delete product
@router.delete("/delete-product/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user= Depends(decode_token)
) -> Dict[str, str]:
    """
    Admin endpoint to delete a product by its ID.
    """
    
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        logger.warning(f"Admin {user.id} tried to delete non-existent product ID {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    if product.created_by != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to modify this product.")
    product.is_deleted = True
    db.commit()
    logger.info(f"Product ID {product_id} deleted by admin {user.id}")
    return {"detail": "Product deleted successfully"}


#users can get products with filters, sorting and pagination

@router.get("/getProductsBySorting", response_model=List[ProductOut])
def list_products(
    category: str = Query(None),
    min_price: float = Query(None, ge=0),
    max_price: float = Query(None, ge=0),
    sort_by: str = Query("id", regex="^(id|price|name|stock)$"),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    user = Depends(decode_token)  # Require authentication

) -> List[ProductOut]:
    """
    User endpoint to get products with optional filters, sorting, and pagination.
    """
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category,Product.is_deleted == False)
    if min_price is not None:
        query = query.filter(Product.price >= min_price, Product.is_deleted == False)
    if max_price is not None:
        query = query.filter(Product.price <= max_price, Product.is_deleted == False)
    sort_column = getattr(Product, sort_by)
    query = query.order_by(sort_column)
    total = query.count()
    products = query.offset((page - 1) * page_size).limit(page_size).all()
    if not products:
        logger.warning("No products found for user filter/search request.")
        raise HTTPException(status_code=404, detail="No products found.")
    logger.info(f"User fetched products with filters. Returned: {len(products)}")
    return products


#users can search products by keyword in name or description
@router.get("/search", response_model=List[ProductOut])
def search_products(
    keyword: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
    user = Depends(decode_token)  # Require authentication

) -> List[ProductOut]:
    """
    User endpoint to search products by keyword in name or description.
    """
    products = db.query(Product).filter(
        or_(
            Product.name.ilike(f"%{keyword}%"),
            Product.description.ilike(f"%{keyword}%")
        )
    ).filter(Product.is_deleted == False).all()
    if not products:
        logger.warning(f"No products found matching search keyword: {keyword}")
        raise HTTPException(status_code=404, detail="No products found matching the search keyword.")
    logger.info(f"User searched for products with keyword '{keyword}'. Found: {len(products)}")
    return products

#user can get all products without any filters
@router.get("/getAllProductsForUser", response_model=List[ProductOut])
def get_all_products_for_user(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1, le=100), 
    db: Session = Depends(get_db),
    user = Depends(decode_token)  # Require authentication

) -> List[ProductOut]:
    """
    User endpoint to get all products with pagination (no filters).
    """
    products = db.query(Product).filter(Product.is_deleted == False).offset(skip).limit(limit).all()
    if not products:
        logger.warning("No products found (user endpoint).")
        raise HTTPException(status_code=404, detail="No products found.")
    logger.info(f"User fetched all products. Total: {len(products)}")
    return products


@router.get("/getProducts/{id}", response_model=ProductOut)
def get_product_detail(
    id: int,
    db: Session = Depends(get_db),
    user = Depends(decode_token)  # Require authentication

) -> ProductOut:
    """
    User endpoint to get product details by product ID.
    """
    product = db.query(Product).filter(Product.id == id,Product.is_deleted == False).first()
    if not product:
        logger.warning(f"User tried to fetch non-existent product ID {id}")
        raise HTTPException(status_code=404, detail="Product not found.")
    logger.info(f"User fetched product ID {id}")
    return product





