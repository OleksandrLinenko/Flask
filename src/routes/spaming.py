from flask import Blueprint
from flask import request
from src.models.spam_message import SpamMessage
from src.database import db

spam_bp = Blueprint("spam", __name__)

@spam_bp.route("/spam", methods=["POST"])
def spam():
    data = request.get_json()

    if data["sensor"] == "fall":
        message = (
            f"Fall detected: {data['detected']}, "
            f"strength: {data['strength']}"
        )

    else:
        message = (
            f"Impact: {data['force']} {data['unit']}"
        )

    spam = SpamMessage(message=message)

    db.session.add(spam)
    db.session.commit()

    return "OK"

@spam_bp.route("/spam/messages")
def spam_messages():
    messages = SpamMessage.query.all()

    return {
        "messages": [
            {
                "id": m.id,
                "message": m.message
            }
            for m in messages
        ]
    }
