from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from config.db import meta, engine

cards = Table(
    'cards',
    meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('edition', String(255), nullable=False),
    Column('language', String(255), nullable=False),
    Column('foil', Boolean(False), nullable=False),
    Column('price', Float, nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
)

meta.create_all(engine)