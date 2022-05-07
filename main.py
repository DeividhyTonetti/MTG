from fastapi import FastAPI

app = FastAPI()

@app.post("/create/")
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

@app.get("/listCard/{name_card}")
async def list_card_by_name(name_card: str):
    return {"item_id": name_card}

@app.get("/listAllCards/")
async def list_all_cards():
    return {"item_id"}

@app.put("/editCard/{name_card}")
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

@app.delete("/deleteCard/{name_card}")
async def list_card_by_name(name_card: str):
    return 0
