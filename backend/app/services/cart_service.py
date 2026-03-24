from sqlalchemy.orm import Session
from app.models import Cart, CartItem, ProductDB
from fastapi import HTTPException


def get_or_create_cart(db : Session,   user_id: int):
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    if not cart:
        cart = Cart(user_id = user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    return cart

def add_to_cart(db: Session, user_id : int, product_id: int, quantity : int = 1):
    cart = get_or_create_cart(db, user_id)

    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    cart_item = db.query(CartItem).filter(CartItem.cart_id == cart.id, CartItem.product_id == product_id).first()

    if cart_item:
        cart_item.quantity+= quantity
    else:
        new_item = CartItem(
            cart_id = cart.id,
            product_id = product.id,
            quantity = quantity
        )
        db.add(new_item)
    db.commit()
    db.refresh(cart)
    return cart

def get_cart(db: Session, user_id: int):
    # “Get cart” should NOT create a cart silently
    return db.query(Cart).filter(Cart.user_id == user_id).first()

def remove_from_cart(db: Session, user_id: int, product_id : int, quantity: int =1):
    cart = get_cart(db, user_id)
    if not cart:
        raise HTTPException(status_code = 404 , detail = "Cart Not Found")
    cart_item = db.query(CartItem).filter(
        CartItem.cart_id== cart.id,
        CartItem.product_id == product_id
    ).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    if cart_item.quantity>quantity:
        cart_item.quantity-=quantity
    else:
        db.delete(cart_item)
    
        
    db.commit()
    db.refresh(cart)
    return cart
