from fastapi import APIRouter


router = APIRouter()

@router.post("/create/")
async def create_card(
    name: str,
    edition: str,
    language: str,
    foil: bool,
    price: float,
    quantity: int,
    parent_id: int,
):

    return 0

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