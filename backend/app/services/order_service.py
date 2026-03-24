from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Cart, CartItem, Order, OrderItem

def place_order(db : Session, user_id : int):
    #1. Get cart
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    #2. Check Empty
    if not cart or not cart.items:
        raise HTTPException(status_code = 404, detail = "Cart is Empty")

    total_price = 0
    #3.Calculate total
    for item in cart.items:
        total_price += item.quantity * item.product.price
    
    #4. Create Order
    order = Order(
        user_id = user_id, 
        total_price = total_price
    )
    db.add(order)
    db.commit() 
    db.refresh(order)

    #5. Move items -> order_items

    for item in cart.items:
        order_item = OrderItem(
            order_id = order.id,
            product_id = item.product.id,
            quantity = item.quantity,
            price_at_time = item.procuct.price 
        )
        db.add(order_item)
    
    #6.Clear cart
    for item in cart.items:
        db.delete(item)
    db.commit()
    return order

def get_order(db : Session, user_id : int):
    orders = db.query(Order).filter(Order.user_id == user_id).first()
    return orders