from fastapi import APIRouter, Depends, Query
from googletrans import Translator
from sqlalchemy.orm import Session
from src.config.db import get_db
# from scheme.schemes import CardScheme
from src.repository.card_repository import CardRepository

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
    name_card: str,
    user_name: str,
    quantity: int = None,
    price: float = None,
    db: Session = Depends(get_db)
):

    translate = Translator()
    idiom = translate.detect(name_card).lang
    name_translated = translate.translate(name_card, src=idiom, dest='pt')

    card_name = name_translated.text
    update_card = CardRepository(db).update(card_name, user_name, quantity, price)

    return update_card

@router.delete("/deleteCard/{name_card}/{name_user}")
async def delete_card(name_card: str, name_user: str, db: Session = Depends(get_db)):
    
    translate = Translator()
    idiom = translate.detect(name_card).lang
    name_translated = translate.translate(name_card, src=idiom, dest='pt')

    name = name_translated.text

    print(name, name_user)
    delete_card = CardRepository(db).delete(name, name_user)

    return delete_card