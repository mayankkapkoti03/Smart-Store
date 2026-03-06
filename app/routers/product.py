from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.services import product_service
from typing import Optional 
from enum import Enum
from app.auth.dependencies import get_current_admin
from app.logger import logger
router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

class SortOrder(str,Enum):
    asc = "asc"
    desc = "desc"   
class SortField(str, Enum):
    id = "id"
    name = "name"
    price = "price"
    quantity = "quantity"


# @router.post("/", dependencies=[Depends(get_current_user)])
# def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
#     return product_service.create_product(db, product)
# def create_product(product: schemas.ProductCreate,db: Session = Depends(get_db),current_user = Depends(get_current_user)):
@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate,db: Session = Depends(get_db),admin = Depends(get_current_admin)):
    logger.info(f"Product created by admin: {admin.email}")
    return product_service.create_product(db, product)



@router.get("/search",response_model = schemas.PaginatedProductResponse)
def search_products(
    name: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price : Optional[float] = None, 
    sort_by : SortField  = SortField.id,
    order : SortOrder = SortOrder.asc,
    limit : int = Query(10, ge=1, le = 100),
    skip : int = Query(0, ge = 0),

    db: Session = Depends(get_db)
):
    products = product_service.search_products(
        db,
        name=name,
        min_price=min_price,
        max_price=max_price,
        sort_by = sort_by.value,
        order = order.value,
        limit = limit,
        skip = skip,
    )
    return products


@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(skip: int = 0,limit: int = 10, db: Session = Depends(get_db)):
    products = product_service.get_all_products(db, skip, limit)
    return products






@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = product_service.get_product_by_id(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product



@router.patch("/{product_id}", response_model=schemas.ProductResponse)
def patch_product(product_id: int, updated_data: schemas.ProductUpdate, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    
    product = product_service.patch_product(db, product_id, updated_data)

    if not product:
        logger.error(f"Product {product_id} not found")
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Product updated: {product_id} by {admin.email}")
    return product

@router.put("/{product_id}", response_model = schemas.ProductResponse)
def update_product(product_id: int, updated_data: schemas.ProductCreate, db: Session = Depends(get_db), admin = Depends(get_current_admin)):

    product = product_service.update_product(db, product_id, updated_data)
    if not product:
        logger.error(f"Product {product_id} not found")
        raise HTTPException(status_code=404, detail="Product not found")
    
    logger.info(f"Product updated: {product_id} by {admin.email}")
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db),admin = Depends(get_current_admin)):

    product = product_service.delete_product(db, product_id)
    if not product:
        logger.error(f"Product {product_id} not found")
        raise HTTPException(status_code=404, detail="Product not found")
    
    logger.info(f"Product deleted: {product_id} by {admin.email}")
    return {"message": "Product deleted successfully"}