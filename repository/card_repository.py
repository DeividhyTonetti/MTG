from sqlalchemy.orm import Session
from scheme import schemes
from models import card_model
from sqlalchemy import desc

class CardRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(
        self, 
        # card: schemes.CardScheme 
        name,
        user_name,
        edition,
        language,
        foil,
        price,
    ):
        db_card = card_model.Card(
            name = name,
            edition = edition,
            language = language,
            foil = foil,
            price= price,
            quantity = 0,
            user_name=user_name,
        )

        self.db.add(db_card)
        self.db.commit()
        self.db.refresh(db_card)

        return db_card

    def list_all(self, user_name: str):
        cards = (
            self.
            db.
            query(card_model.Card).
            filter(card_model.Card.user_name==user_name).
            order_by(desc(card_model.Card.price)).
            all()
        )
        
        return cards
    
    def list_by_name(self, card_name: str, user_name: str):
        cards = (
            self.
            db.
            query(card_model.Card).
            filter(card_model.Card.name==card_name, card_model.Card.user_name==user_name).
            order_by(desc(card_model.Card.price)).
            all()
        )
        
        return cards


    def update(
        self, 
            card_name: str, 
            user_name: str, 
            quantity: int,
            price: float
        ):

        cards = (
            self.
            db.
            query(card_model.Card).
            filter(card_model.Card.name==card_name, card_model.Card.user_name==user_name).
            update({card_model.Card.quantity: quantity, card_model.Card.price: price})
        )

        self.db.commit()
        
        return cards

    def delete(self, card_name: str, user_name: str):
        cards = (
            self.
            db.
            query(card_model.Card).
            filter(card_model.Card.name==card_name, card_model.Card.user_name==user_name).
            delete()
        )

        self.db.commit()
        
        return cards