from fastapi import APIRouter, Depends, Query
from googletrans import Translator
from sqlalchemy.orm import Session
from config.db import get_db
from scheme.schemes import CardScheme
from repository.card_repository import CardRepository

router = APIRouter()

@router.post("/create")
async def create_card(
    # card: CardScheme,  Com esquema (porém o formato para usuário é json)
    # language: str = Query('Português', enum=['Português', 'Inglês', 'Japonês']), O usuário nâo precisa saber
    name: str,
    user_name: str,
    edition: str,
    foil: bool = False,
    price: float = 0,
    db: Session = Depends(get_db)
):

    translate = Translator()
    idiom = translate.detect(name).lang
    name_translated = translate.translate(name, src=idiom, dest='pt')

    name = name_translated.text
    language = idiom

    created_card = CardRepository(db).create(
        name,
        user_name,
        edition,
        language,
        foil,
        price,
    )

    return created_card

@router.get("/listCard/{name_card}/{name_user}")
async def list_card_by_name(name_card: str, name_user: str, db: Session = Depends(get_db)):
    
    translate = Translator()
    idiom = translate.detect(name_card).lang
    name_translated = translate.translate(name_card, src=idiom, dest='pt')

    name = name_translated.text

    list_card = CardRepository(db).list_by_name(name, name_user)
    
    return {"item_id": list_card}

@router.get("/listAllCards")
async def list_all_cards(user_name: str, db: Session = Depends(get_db)):
    list_all = CardRepository(db).list_all(user_name)

    return list_all

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