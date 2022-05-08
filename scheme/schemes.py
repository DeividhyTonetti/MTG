from email.mime import base
from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import Optional

class UserScheme(BaseModel):
    id: Optional[str] = None
    name: str

    class Config:
        orm_mode = True

class CardScheme(BaseModel):
    id: Optional[str] = None
    edition: str
    language: str
    foil: bool
    price: float = False
    quantity: int
    parent_id: str

    class Config:
        orm_mode = True