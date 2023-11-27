"""Main module for the application."""

from repositories.user_repository import user_repository
from services.user_service import user_service
import sql_queries
from os import getenv
from extensions import db, app
from flask import Flask, render_template, request, redirect, url_for, flash


def redirect_to_login():
    """Redirect to login page."""
    return redirect(url_for("render_login"))

def redirect_to_register():
    """Redirect to register page."""
    return redirect(url_for("render_register"))


def redirect_to_new_citation():
    """Redirect to new citation page."""
    return redirect(url_for("render_new_citation"))

def redirect_to_index():
    """Redirect to index page."""
    return redirect(url_for("render_home"))


@app.route("/")
def render_home():
    """Render home page."""
    citates = sql_queries.all_references_from_db()
    #list to dict
    if citates is None:
        citates_dict = {}
    else:
        citates_dict = {idx: reference for idx, reference in enumerate(citates)}
        
    return render_template("index.html", citates=citates_dict)


@app.route("/login", methods=["GET"])
def render_login():
    """Render login form."""
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():
    """Handle login form."""
    username = request.form.get("username")
    password = request.form.get("password")

    try:
        user_service.check_credentials(username, password)
        return redirect_to_index()
    except Exception as error:
        flash(str(error))
        return redirect_to_login()


@app.route("/logout", methods=["POST"])
def logout():
    """Logout."""
    return redirect_to_login()

@app.route("/new_reference", methods=['GET', 'POST'])
def new_reference():
    """Render form."""
    selected_type = request.form.get('ra', 'Article')
    return render_template("form.html", selected_type=selected_type)


@app.route("/add_reference", methods=["GET"])
def render_form():
    """Render form."""
    render_template("form.html")

@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    """Add reference to database."""
    #ONLY WORKS WITH ARTICLE TYPE
    # cretae a new reference into a dict
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        article = {
        "author": request.form.get("author"),
        "title": request.form.get("title"),
        "journal": request.form.get("journal"),
        "year": request.form.get("year"),
        "volume": request.form.get("volume"),
        "number": request.form.get("number"),
        "pages": request.form.get("pages"),
        "month": request.form.get("month"),
        "doi": request.form.get("doi"),
        "note": request.form.get("note"),
        "key": request.form.get("key")}
        sql_queries.article_to_db(article)
        return render_template("index.html", citates=article)
    else:
        return "Invalid request method"




@app.route("/register", methods=["GET"])
def render_register():
    """Render register form."""
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def handle_register():
    """Register a new user."""
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")

    try:
        user_service.create_user(username, password, password_confirmation)
        return redirect_to_login
    except Exception as error:
        flash(str(error))
        return redirect_to_register()


# sovelluksen tilan alustaminen testejä varten
@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    user_repository.delete_all()
    return "Reset"

@app.route("/edit_reference", methods=["GET", "POST"])
def edit_reference():
    # info = sql_queries.edit_reference()
    # pitää hakea halutun viitteen tiedot tietokannasta! -> tallenna tiedot listaan "info=[]"
    # info=info
    return render_template("edit.html")


@app.route("/make_changes", methods=["GET", "POST"])
def make_changes():
    author = request.form["name"]
    title = request.form["title"]
    book_title = request.form["book_title"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volme"]
    pages = request.form["pages"]
    publisher = request.form["publisher"]
    sql_queries.make_changes(
        author, title, book_title, journal, year, volume, pages, publisher)
    return render_template("index.html")


@app.route("/delete_reference", methods=["GET", "POST"])
def delete_reference():
    # TODO 
    pass

