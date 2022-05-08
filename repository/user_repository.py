from sqlalchemy.orm import Session
from scheme import schemes
from models import user_model

class UserRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, user: schemes.UserScheme):
        db_user = user_model.Card(name= user.name)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh()

        return db_user

    def list(self):
        users = self.db.query(user_model.Card).all()
        
        return users


    def update(self):
        pass

    def delete(self):
        pass