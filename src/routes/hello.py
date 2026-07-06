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

@hello_bp.route("/hi/")
@hello_bp.route("/hi/<name>")
def hi(name=None):
    message = user_service.greet(name)
    users = user_service.get_users()

    flash(message)
    return render_template(
        "hi.html",
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
    user_service.create_user(name)

    return redirect("/hi")

@hello_bp.route("/users/edit", methods=["POST"])
def update_user():

    user_id = request.form.get("id")
    name = request.form.get("name")

    user_service.update_user(user_id, name)

    return redirect("/hi")

