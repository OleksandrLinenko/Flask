from flask import Blueprint
from flask import request
from flask import render_template
about_bp = Blueprint("about", __name__)

@about_bp.route("/about")
def about():
    return render_template("about_template.html")
