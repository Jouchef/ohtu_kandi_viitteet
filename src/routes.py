"""Main module for the application."""

from repositories.user_repository import user_repository
from services.user_service import user_service
import sql_queries
from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app
import psycopg2

# Initialize the SQLAlchemy object without directly associating it with the app
# make conn and cur global variable so that they can be used in other functions


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


# @app.route("/")
# def render_home():
   # conn = psycopg2.connect(
    # database="ohtu", user="postgres", host="localhost", port="5432")
    # cur = conn.cursor()
   # cur.execute('''SELECT * FROM references_table''')  # where visible = True

    # Fetch the data
    # data = cur.fetchall()

    # cur.close()
    # conn.close()
    # return render_template('index.html', citates=data)

@app.route("/")
def render_home():
    return render_template("login_and_register.html")


@app.route("/form", methods=["GET", "POST"])
def add_reference():
    """Add reference to database."""
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        conn = psycopg2.connect(
            database="ohtu", user="postgres", host="localhost", port="5432")
        cur = conn.cursor()
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
        # insert the data into the table
        visible = True
        cur.execute(
            '''INSERT INTO references_table (visible, author, title, journal, year, volume, number, pages, month, doi, note, key)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
            (visible, author, title, journal, year, volume, number, pages, month, doi, note, key))
        conn.commit()
        # citations = cur.fetchall()
        # print(citations)
        # close the cursor and connection
        cur.close()
        conn.close()

        # call the function to render the index page with the citations
        return redirect_to_index()


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle login form."""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
        if sql_queries.login(username, password):
            session["username"] = username
            return render_template("index.html")
        else:
            return render_template("error.html", message=("wrong username"))
    else:
        return render_template("login.html")


@app.route("/logout", methods=["POST"])
def logout():
    """Logout."""
    return redirect_to_login()


@app.route("/edit/<int:reference_id>", methods=["GET", "POST"])
def editprofile(reference_id):
    """Edit preferencese from database using form and id."""
    if request.method == 'GET':
        # get the reference from the database
        conn = psycopg2.connect(
            database="ohtu", user="postgres", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM references_table WHERE id = %s''',
                    (reference_id,))  # this returns a list of tuples

        reference = cur.fetchone()
        cur.close()
        conn.close()
        # render the edit page with the reference
        if reference[2] == True:
            return render_template('edit.html', reference=reference)
        else:
            return redirect_to_index()

    if request.method == 'POST':
        conn = psycopg2.connect(
            database="ohtu", user="postgres", host="localhost", port="5432")
        cur = conn.cursor()
        try:
            cur.execute(
                '''SELECT * FROM references_table WHERE id = %s''', (reference_id,))
            reference = cur.fetchone()
            if reference[2] == True and reference is not None:

                print(reference)
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
                # update the reference in the database
                cur.execute('''UPDATE references_table SET author = %s, title = %s, journal = %s, year = %s, volume = %s, number = %s, pages = %s, month = %s, doi = %s, note = %s, key = %s WHERE id = %s''',
                            (author, title, journal, year, volume, number, pages, month, doi, note, key, reference_id))
                conn.commit()
                cur.close()
                conn.close()
                # redirect to the index page
                return redirect_to_index()
            else:
                # render index page with error message
                return render_home()
        except Exception as error:
            print(error)
            # call the function to render the index page with the updated reference
            return render_home()


# Maijan uusi register (toimii)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form["username"]
    password = request.form["password"]
    if sql_queries.register(username, password):
        return render_template("login_and_register.html")
    else:
        return render_template("error.html", message=(f"This username already exists: {username}"))


# sovelluksen tilan alustaminen testejä varten
@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    user_repository.delete_all()
    return "Reset"


@app.route("/new_reference", methods=['GET', 'POST'])
def new_reference():
    """Render form."""
    selected_type = request.form.get('ra', 'Article')
    return render_template("form.html", selected_type=selected_type)


@app.route("/delete_reference/<int:reference_id>", methods=["GET", "POST"])
def delete_reference(reference_id):
    try:
        sql_queries.delete_reference(reference_id)
        sql_queries.ids_list()
        return redirect_to_index()
    except Exception as error:
        flash(str(error))
        return redirect_to_index()

    # jos onnistuu, anna käyttäjälle ilmo et deletion completed! etc


# @app.route("/delete_reference", methods=["GET", "POST"])
# def delete_reference():
    # TODO
    # pass
