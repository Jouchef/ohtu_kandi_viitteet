"""Main module for the application."""

from repositories.user_repository import user_repository
from services.user_service import user_service
import sql_queries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app
import psycopg2

# Initialize the SQLAlchemy object without directly associating it with the app
# make conn and cur global variable so that they can be used in other functions
conn = psycopg2.connect(database="ohtu", user="postgres", host="localhost", port="5432")

cur = conn.cursor()

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
    conn = psycopg2.connect(database="ohtu", user="postgres", host="localhost", port="5432")

    cur = conn.cursor()

    cur.execute('''SELECT * FROM references_table''')

    # Fetch the data
    data = cur.fetchall()

    cur.close()
    conn.close()
    print(data)
    return render_template('index.html', citates=data) 

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
        return redirect_to_index()


@app.route("/logout", methods=["POST"])
def logout():
    """Logout."""
    return redirect_to_login()

@app.route("/form", methods=["GET","POST"])
def add_reference():
    """Add reference to database."""
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        # create a dictionary from the form data
        author = request.form.get("author")
        title = request.form.get("title")
        journal = request.form.get("journal")
        year = request.form.get("year")
        volume = request.form.get("volume")
        number = request.form.get("number")
        pages = request.form.get("pages")
        month = request.form.get("month")
        doi = request.form.get("doi")
        note = request.form.get("note")
        key = request.form.get("key")
        article = {
            "author": author,
            "title": title,
            "journal": journal,
            "year": year,
            "volume": volume,
            "number": number,
            "pages": pages,
            "month": month,
            "doi": doi,
            "note": note,
            "key": key
        }
        sql_queries.article_to_db(article)
        # get the citations from the database
        citations = sql_queries.all_references_from_db()
        print(citations)
        # call the function to render the index page with the citations 
        return redirect_to_index()




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
