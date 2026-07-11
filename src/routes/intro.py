from flask import Blueprint
from flask import request
from flask import render_template
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService

intro_bp = Blueprint("intro", __name__)

@intro_bp.route("/")
def hello_world():
    return render_template("index.html")

@intro_bp.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return render_template("hello.html", name=name)
