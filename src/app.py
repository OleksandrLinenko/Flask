from flask import Flask
from flask import request
from markupsafe import escape
from .routes.about import about_bp
from src.routes.hello import hello_bp
from src.database import db
from src.models.user import User

app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if User.query.count() == 0:
        db.session.add_all([
            User(name="Bob", password="123"),
            User(name="John", password="456"),
            User(name="Bill", password="789")
        ])
        
        db.session.commit()

app.register_blueprint(about_bp)
app.register_blueprint(hello_bp)






