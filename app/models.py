from sqlalchemy import Column, Integer, String, Float
from .database import Base   # VERY IMPORTANT

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

