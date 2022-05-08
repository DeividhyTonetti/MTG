from pydantic import BaseModel
from typing import Optional

class CardScheme(BaseModel):
    id: Optional[str] = None
    name: str
    edition: str
    language: str
    foil: bool
    price: float = False
    quantity: int
    user_id: str

    class Config:
        orm_mode = True