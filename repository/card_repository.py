from sqlalchemy.orm import Session
from scheme import schemes
from models import card_model

class CardRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, card: schemes.CardScheme):
        db_card = card_model.Card(
            name= card.name,
            edition= card.edition,
            language= card.language,
            foil= card.foil,
            price= card.price,
            quantity= card.quantity,
            user_id= card.user_id,
        )

        self.db.add(db_card)
        self.db.commit()
        self.db.refresh(db_card)

        return db_card

    def list(self):
        cards = self.db.query(card_model.Card).all()
        
        return cards


    def update(self):
        pass

    def delete(self):
        pass