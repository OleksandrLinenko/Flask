from src.database import db


class SpamMessage(db.Model):
    __tablename__ = "spam_messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    