"""Module to handle user routes"""
# import secrets
from flask import (render_template,
                   redirect,
                   session, request,
                   Blueprint,
                   flash)  # pylint: disable=import-error unused-import
# from flask_wtf.csrf import generate_csrf # pylint: disable=import-error unused-import
from services.reference_service import ReferenceService as reference_service  # pylint: disable=import-error no-name-in-module

from services.user_service import UserService  # pylint: disable=import-error no-name-in-module
from services.user_service import UserInputError, AuthenticationError
user_service = UserService()
users = Blueprint("users", __name__)


@users.route("/", methods=["GET"])
def render_home():
    """Render home page for user with all of their references."""
    user_id = session.get("user_id")
    if user_id:
        referenc_serv = reference_service()
        references = referenc_serv.get_all_references_by_user_id(user_id)
    else:
        user_id = None
        references = []
        print("No user id")
    return render_template("index.html", references=references, user_id=user_id)


@users.route("/login", methods=["GET"])
def render_login():
    """Render login page."""
    return render_template("login.html")


@users.route("/login", methods=["POST"])
def login():
    """Call the function to check credentials and log in user."""
    username = request.form["username"]
    password = request.form["password"]

    try:
        user = user_service.check_credentials(username, password)
        session["username"] = username
        session["user_id"] = user.id
        return redirect("/")

    except (AuthenticationError, UserInputError) as error:
        flash(str(error))
        return render_template("login.html")


@users.route("/logout", methods=["POST"])
def logout():
    """Log out user."""
    session.pop("username", None)
    session.pop("user_id", None)
    return render_template("index.html")


@users.route("/register", methods=["GET"])
def render_register():
    """Render register page."""
    return render_template("register.html")


@users.route("/register", methods=["POST"])
def register():
    """Register user."""
    username = request.form["username"]
    password = request.form["password"]
    password_confirmation = request.form["password_confirmation"]
    try:
        user_service.create_user(username, password, password_confirmation)
        print("User created successfully")
        return render_template("login_and_register.html")
    except Exception as error:  # pylint: disable=broad-except
        print("Error: ", error)
        return render_template("register.html")


@users.route("/ping")
def ping():
    """Ping for testing purposes."""
    return "Pong"
