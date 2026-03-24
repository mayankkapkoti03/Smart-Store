from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.ProductDB)\
             .filter(models.ProductDB.id == product_id)\
             .first()


def get_all_products(db: Session, skip: int, limit: int):
    return db.query(models.ProductDB).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, updated_data: schemas.ProductCreate):
    product = db.query(models.ProductDB)\
                .filter(models.ProductDB.id == product_id)\
                .first()

    if product is None:
        return None

    product.name = updated_data.name
    product.price = updated_data.price
    product.quantity = updated_data.quantity

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int):
    product = db.query(models.ProductDB)\
                .filter(models.ProductDB.id == product_id)\
                .first()

    if product is None:
        return None

    db.delete(product)
    db.commit()
    return product


def patch_product(db: Session, product_id: int, updated_data: schemas.ProductUpdate):
    product = db.query(models.ProductDB).filter(models.ProductDB.id == product_id).first()

    if not product:
        return None

    update_fields = updated_data.dict(exclude_unset=True)

    for key, value in update_fields.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product



def search_products(
    db: Session,
    name: str | None = None,
    min_price: float | None = None,
    max_price : float | None = None,
    sort_by : str = "id",
    order : str = "asc",
    limit : int = 10,
    skip : int = 0
):
    query = db.query(models.ProductDB)
    if min_price is not None and max_price is not None:
        if min_price > max_price:
            raise HTTPException(status_code=400,detail="min_price cannot be greater than max_price")
    if name: 
        query = query.filter(models.ProductDB.name.ilike(f"%{name}%"))
    if min_price is not None:
        query = query.filter(models.ProductDB.price>=min_price)
    if max_price is not None:
        query = query.filter(models.ProductDB.price<=max_price)
    
    #Sorting
    
    column = getattr(models.ProductDB, sort_by)
    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())
    # #Pagination
    total = query.count()
    items = query.offset(skip).limit(limit).all()
    return {
        "total" : total,
        "items" : items
    }