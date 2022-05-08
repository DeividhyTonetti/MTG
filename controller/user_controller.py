from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from scheme.schemes import UserScheme
from repository.user_repository import UserRepository

router = APIRouter()

@router.post("/create")
async def create_card(card: UserScheme, db: Session = Depends(get_db)):
    created_user= UserRepository(db).create(card)

    return created_user

@router.get("/listUser/{name_user}")
async def list_card_by_name(name_card: str):
    return {"item_id": name_card}

@router.get("/listAllUsers/")
async def list_all_cards():
    return {"item_id"}

@router.put("/editUsers/{name_user}")
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

@router.delete("/deleteUsers/{name_user}")
async def list_card_by_name(name_card: str):
    return 0