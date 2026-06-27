from flask import Flask
from flask import request
from markupsafe import escape
from .routes.about import about_bp
from src.routes.hello import hello_bp

app = Flask(__name__)
app.secret_key = "my_secret_key"

app.register_blueprint(about_bp)
app.register_blueprint(hello_bp)






