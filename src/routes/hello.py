from flask import Blueprint
from flask import request
from markupsafe import escape
from flask import render_template
from flask import flash, redirect, url_for
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from flask import jsonify

hello_bp = Blueprint("hello", __name__)
user_repo = UserRepository()
user_service = UserService(user_repo)

@hello_bp.route("/")
def hello_world():
    return render_template("index.html")

@hello_bp.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return render_template("hello.html", name=name)

@hello_bp.route("/users/")
@hello_bp.route("/users/<name>")
def users(name=None):
    message = user_service.greet(name)
    users = user_service.get_users()

    flash(message)
    return render_template(
        "users.html",
        users=users,
        person=name
    )

@hello_bp.route("/api/users")
def get_users():
    users = user_service.get_users()

    return jsonify([
        {
            "id": user.id,
            "name": user.name
        }
        for user in users
    ])

@hello_bp.route("/api/users/<int:user_id>")
def get_user(user_id):

    user = user_service.get_user(user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name
    })

@hello_bp.route("/users", methods=["POST"])
def create_user():
    name = request.form.get("name")
    password = request.form.get("password")
    user_service.create_user(name, password)

    return redirect("/users")

@hello_bp.route("/users/<int:user_id>/edit", methods=["POST"])
def update_user(user_id):
    name = request.form.get("name")
    user_service.update_user(user_id, name)

    return redirect("/users")

@hello_bp.route("/login", methods=["POST"])
def login():
    name = request.form.get("name")
    password = request.form.get("password")

    if user_service.login(name, password):
        flash("Successfully logged in!")
    else:
        flash("Wrong username or password!")

    return redirect("/users")

@hello_bp.route("/users/<int:user_id>/edit")
def edit_user(user_id):

    user = user_service.get_user(user_id)

    if user is None:
        flash("User not found")
        return redirect("/users")

    return render_template(
        "edit_user.html",
        user=user
    )
