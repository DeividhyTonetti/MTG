from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base
from models import card_model

class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(255), nullable=False)

    cards = relationship(card_model.Card, back_populates="user")