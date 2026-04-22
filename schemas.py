from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class ProductBase(BaseModel):
    name: str
    price: float

class OrderBase(BaseModel):
    product_name: str
    quantity: int

class UserCreate(UserBase): pass
class ProductCreate(ProductBase): pass
class OrderCreate(OrderBase): pass