from src.models.user import User
from src.database import db

class UserRepository:

    def get_users(self):
        return User.query.all()

    def find_user(self, name):
        return User.query.filter_by(name=name).first()

    def add_user(self, name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
    