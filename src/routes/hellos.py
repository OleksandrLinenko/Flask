from flask import Blueprint
from flask import request
from markupsafe import escape
from flask import render_template
from flask import flash, redirect, url_for
from src.repositories.hello_repository import HelloRepository

hellos_bp = Blueprint("hellos", __name__)
hellos_repo = HelloRepository()

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
    users = hellos_repo.get_users()

    if hellos_repo.find_user(name):
        flash(f"Hello, {name}!")
    elif name:
        flash(f"Hello, {name}!")
    else:
        flash(f"User not found")

    return render_template("hello.html", users=users, person=name)
