from flask import Flask
from src.routes.intro import intro_bp
from src.routes.about import about_bp
from src.routes.auth import auth_bp
from src.routes.users import users_bp
from src.routes.spaming import spam_bp
from src.database import db
from src.models.user import User
from werkzeug.security import generate_password_hash
from src.models.spam_message import SpamMessage

app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if User.query.count() == 0:
        db.session.add_all([
            User(name="Bob", password=generate_password_hash("123")),
            User(name="John", password=generate_password_hash("456")),
            User(name="Bill", password=generate_password_hash("789"))
        ])
        
        db.session.commit()

app.register_blueprint(intro_bp)
app.register_blueprint(about_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(spam_bp)
