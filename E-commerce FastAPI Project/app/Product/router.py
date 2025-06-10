from fastapi import APIRouter, Depends, HTTPException, status,Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.Product.models import Product
from app.Product.schemas import ProductCreate,ProductOut
from app.utils.oauth2 import decode_token
from fastapi.security import OAuth2PasswordBearer
from typing import List
from sqlalchemy import or_


router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin")

#for checking if the user is admin
def get_current_user_role(token: str = Depends(oauth2_scheme)):
    data = decode_token(token)
    if not data or data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return data

# admin can create a product
@router.post("/create-product", status_code=status.HTTP_201_CREATED, response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user_role)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


#admin can get all products
@router.get("/getAllProducts", response_model=List[ProductOut])
def get_all_products(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1,le=100), 
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user_role)  
):
    products = db.query(Product).offset(skip).limit(limit).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found.")
    return products


#admin can get product by id
@router.get("/getProductById/{product_id}", response_model=ProductOut)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user_role)  # <-- Only admins can access
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

#admin can update product details 
@router.put("/update-product/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user_role)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.stock = product.stock
    existing_product.category=product.category
    existing_product.image_url = product.image_url
    db.commit()
    db.refresh(existing_product)
    return existing_product

#admin can delete product
@router.delete("/delete-product/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(product_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user_role)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
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
):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    # Sorting
    sort_column = getattr(Product, sort_by)
    query = query.order_by(sort_column)

    # Pagination
    total = query.count()
    products = query.offset((page - 1) * page_size).limit(page_size).all()

    if not products:
        raise HTTPException(status_code=404, detail="No products found.")

    return products


#users can search products by keyword in name or description
@router.get("/search", response_model=List[ProductOut])
def search_products(
    keyword: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    products = db.query(Product).filter(
        or_(
            Product.name.ilike(f"%{keyword}%"),
            Product.description.ilike(f"%{keyword}%")
        )
    ).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found matching the search keyword.")
    return products

#user can get all products without any filters
@router.get("/getAllProductsForUser", response_model=List[ProductOut])
def get_all_products(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1,le=100), 
    db: Session = Depends(get_db),
):
    products = db.query(Product).offset(skip).limit(limit).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found.")
    return products

#users can get product details by id
@router.get("/getProducts/{id}", response_model=ProductOut)
def get_product_detail(
    id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product






