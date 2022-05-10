from pydantic import BaseModel
from typing import Optional

# TODO: Poderia definir todos os equemas separados de toda aplicação, mas não é esse o intuito
class CardScheme(BaseModel):
    id: Optional[str] = None
    name: str
    edition: str
    language: str = 'português' or 'inglês' or 'japonês'
    foil: bool = False
    price: float = 0
    quantity: int
    user_name: str

    class Config:
        orm_mode = True