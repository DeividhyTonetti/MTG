from fastapi import APIRouter
from controller import card_controller as card
from controller import user_controller as user

router = APIRouter()
router.include_router(user.router, prefix='/user')
router.include_router(card.router, prefix='/card')