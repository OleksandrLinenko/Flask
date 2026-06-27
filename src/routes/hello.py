from flask import Blueprint
from flask import request
from markupsafe import escape
from flask import render_template
from flask import flash, redirect, url_for
from src.repositories.hello_repository import HelloRepository
from src.services.hello_service import HelloService

hello_bp = Blueprint("hello", __name__)
hello_repo = HelloRepository()
hello_service = HelloService(hello_repo)

@hello_bp.route("/")
def hello_world():
    return render_template("index.html")

@hello_bp.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return render_template("hello.html", name=name)

@hello_bp.route('/hi/')
@hello_bp.route('/hi/<name>')
def hi(name=None):
    message = hello_service.greet(name)
    users = hello_service.get_users()

    flash(message)
    return render_template("hi.html", users=users, person=name)
