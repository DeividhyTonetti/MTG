from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from scheme.schemes import CardScheme
from repository.card_repository import CardRepository

router = APIRouter()

@router.post("/create")
async def create_card(card: CardScheme, db: Session = Depends(get_db)):
    created_card = CardRepository(db).create(card)

    return created_card

@router.get("/listCard/{name_card}")
async def list_card_by_name(name_card: str):
    return {"item_id": name_card}

@router.get("/listAllCards/")
async def list_all_cards():
    return {"item_id"}

@router.put("/editCard/{name_card}")
async def update_card(
    name: str,
    edition: str,
    language: str,
    foil: bool,
    price: float,
    quantity: int,
    parent_id: int
):
    return {"item_name"}

@router.delete("/deleteCard/{name_card}")
async def list_card_by_name(name_card: str):
    return 0