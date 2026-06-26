from flask import Blueprint
from flask import request
from markupsafe import escape
from flask import render_template
from flask import flash, redirect, url_for

hellos_bp = Blueprint("hellos", __name__)

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
    users = ["Alice", "Bob", "Charlie"]

    if name:
        flash(f"Hello, {name}!")
    else:
        flash("Hello, anonymous user!")

    return render_template(
        'hello.html',
        person=name,
        users=users
    )