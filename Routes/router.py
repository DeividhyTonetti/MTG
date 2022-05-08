from fastapi import APIRouter
from controller import card_controller as card

router = APIRouter()
router.include_router(card.router, prefix='/card')