from sys import prefix
from fastapi import APIRouter
from controller import home_controller as home

router = APIRouter()
router.include_router(home.router, prefix='/home')