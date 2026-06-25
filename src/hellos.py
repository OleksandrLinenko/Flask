from flask import Blueprint
from flask import request
from markupsafe import escape

hellos_bp = Blueprint("hellos", __name__)

@hellos_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@hellos_bp.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"