from src.models.user import User
from src.database import db
from werkzeug.security import generate_password_hash

class UserRepository:

    def get_users(self):
        return User.query.all()

    def find_user(self, name):
        return User.query.filter_by(name=name).first()

    def add_user(self, name, password):
        user = User(
            name=name,
            password=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

    def get_user(self, user_id):
        return User.query.get(user_id)
    
    def create_user(self, name, password):
        user = User(
            name=name,
            password=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

    def update_user(self, user_id, name):
        user = User.query.get(user_id)

        if user:
            user.name = name
            db.session.commit()
    