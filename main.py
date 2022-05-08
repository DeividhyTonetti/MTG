from fastapi import FastAPI
from Routes.router import router
from config.db import create_db

create_db()

app = FastAPI(
    title='Magic The Gathering',
    description='Crud simples de game de cartas :)',
    version='0.0.1',
    contact={
        'Name': 'Deividhy J. Tonetti',
        'Email': 'deividhytonetti@hotmail.com',
        'whats': '(+55) (12) 9 8296-7213 '
    }
)

app.include_router(router, prefix='')