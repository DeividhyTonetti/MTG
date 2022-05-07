from fastapi import FastAPI
from Routes.router import router

app = FastAPI()
app.include_router(router, prefix='')