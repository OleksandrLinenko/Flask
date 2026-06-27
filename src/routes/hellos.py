from flask import Blueprint
from flask import request
from markupsafe import escape
from flask import render_template
from flask import flash, redirect, url_for
from src.repositories.hellos_repository import HelloRepository
from src.services.hellos_service import HelloService

hellos_bp = Blueprint("hellos", __name__)
hellos_repo = HelloRepository()
hellos_service = HelloService(hellos_repo)

@hellos_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@hellos_bp.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@hellos_bp.route('/hi/')
@hellos_bp.route('/hi/<name>')
def hi(name=None):
    message = hellos_service.greet(name)
    users = hellos_service.get_users()

    flash(message)
    return render_template("hello.html", users=users, person=name)
