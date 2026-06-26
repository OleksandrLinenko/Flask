from flask import Blueprint
from flask import request
about_bp = Blueprint("about", __name__)

@about_bp.route("/about")
def about():
    name = request.args.get("name", "Flask")
    return "<p>The project page of Flask training</p>"
