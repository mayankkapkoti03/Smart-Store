from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.cart_service import add_to_cart, get_cart, get_or_create_cart, remove_from_cart
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/cart", tags = ["Cart"])

@router.post("/add")
def add_item(product_id : int, quantity : int = 1, db : Session = Depends(get_db), user = Depends(get_current_user)):
    return add_to_cart(db,user.id, product_id, quantity)

@router.get("/")
def view_cart(db : Session = Depends(get_db), user = Depends(get_current_user)):
    cart = get_cart(db, user.id)
    if not cart:
        return {"message": "cart is empty"}
    
    return cart

@router.delete("/remove/{product_id}")
def remove_item(product_id : int, quantity : int = 1, db : Session = Depends(get_db), user = Depends(get_current_user)):
    return remove_from_cart(db, user.id, product_id, quantity)