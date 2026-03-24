from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from .database import Base   # VERY IMPORTANT
from sqlalchemy.orm import relationship

class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)



#UserDB model for storing user information in the database. It includes fields for id, email, and hashed_password. The email field is unique to prevent duplicate registrations, and the hashed_password field is used to store the securely hashed version of the user's password.
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default = "user")

#Cart Model
class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default = lambda: datetime.now(timezone.utc))
    items = relationship("CartItem", back_populates = "cart")
    user = relationship("userDB")

#CartItem model
class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key = True, index = True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default = 1)

    cart = relationship("Cart", back_populates = "items")
    product = relationship("ProductDB")

#Order Model
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_price = Column(Float)
    status = Column(String, default = "pending")
    created_at = Column(DateTime, default = lambda: datetime.now(timezone.utc))

    items = relationship("OrderItem", back_populates= "order")
    user = relationship("userDB")

#OrderItem model
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price_at_time = Column(Float)

    order = relationship("Order", back_populates="items")
    product = relationship("ProductDB")