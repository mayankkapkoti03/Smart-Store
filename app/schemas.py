from pydantic import BaseModel, Field, EmailStr
from typing import List , Optional


#Schemas for Product Management
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductResponse(BaseModel):
    name : str
    price : float
    quantity : int
    

class PaginatedProductResponse(BaseModel):
    total : int
    items : List[ProductResponse]
    model_config = {
        "from attributes" : True
    }


class Product(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


#Schemas for User Registration and Login
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    model_config = {
        "from_attributes": True
    }

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str