from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Float
from config.db import Base

class Card(Base):
    __tablename__ = 'card'
    
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(255), nullable=False)
    edition = Column('edition', String(255), nullable=False)
    language = Column('language', String(255), nullable=False)
    foil = Column('foil', Boolean(False), nullable=False)
    price = Column('price', Float, nullable=False)
    quantity = Column('quantity', Integer, nullable=False)
    user_name = Column('user_name', String(255), nullable=False)