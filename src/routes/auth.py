from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from flask import redirect
from flask import session
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService

auth_bp = Blueprint("auth", __name__)
auth_repo = UserRepository()
login_service = UserService(auth_repo)

@auth_bp.route("/login")
def login_page():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    name = request.form.get("name")
    password = request.form.get("password")

    if login_service.login(name, password):
        session["username"] = name
        flash("Successfully logged in!")
        return redirect("/hello")

    flash("Wrong username or password!")
    return redirect("/login")

@auth_bp.route("/logout")
def logout():
    session.pop("username", None)
    flash("Successfully logged out!")
    return redirect("/hello")
