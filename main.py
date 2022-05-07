from fastapi import FastAPI

app = FastAPI()

@app.post("/create/")
def create_card(
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
def list_card_by_name(name_card: str):
    return {"item_id": name_card}

@app.get("/listAllCards/")
def list_all_cards():
    return {"item_id"}

@app.put("/editCard/{name_card}")
def update_card(
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
def list_card_by_name(name_card: str):
    return 0
