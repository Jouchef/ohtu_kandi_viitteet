"""Main module for the application."""

from repositories.user_repository import user_repository
from services.user_service import user_service
import sql_queries
from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from app import app
import psycopg2


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
    conn = psycopg2.connect(
        database="ohtu", user="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    # select all references from the database from the table references_table
    # which are visible and have the id of the user who is logged in


    cur.execute('''SELECT * FROM references_table WHERE visible = True''')
    
    data = cur.fetchall()

    cur.close()
    conn.close()
    return render_template('index.html', citates=data)


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
        reference_type = request.form.get("type")
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
        visible = True
        cur.execute(
            '''INSERT INTO references_table (type, visible, author, title, journal, year, volume, number, pages, month, doi, note, key)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', #pylint: disable=line-too-long
            (reference_type, visible, author, title, journal, year, volume, number, pages, month, doi, note, key)) 
        conn.commit()
        cur.close()
        conn.close()
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
            return render_template("error.html", message="wrong username")
    else:
        return render_template("login.html")
@app.route("/logout", methods=["POST"])
def logout():
    """Logout."""
    return redirect_to_login()


@app.route("/edit/<int:reference_id>", methods=["GET", "POST"])
def edit_reference(reference_id):
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

            # if they clicked the delete button
            if request.form.get('delete') == 'delete':
                cur.execute(
                    '''UPDATE references_table SET visible = False WHERE id = %s''', (reference_id,))
                conn.commit()
                cur.close()
                conn.close()
                return redirect_to_index()


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
                cur.execute('''UPDATE references_table SET author = %s, title = %s, journal = %s, year = %s, volume = %s, number = %s, pages = %s, month = %s, doi = %s, note = %s, key = %s WHERE id = %s''',
                            (author, title, journal, year, volume, number, pages, month, doi, note, key, reference_id))
                conn.commit()
                cur.close()
                conn.close()
                return redirect_to_index()
            else:
                return render_home()
        except Exception as error:
            print(error)
            return render_home()


# Maijan uusi register (toimii)
@app.route("/register", methods=["GET", "POST"])
def register():
    """Handle register form."""
    if request.method == "GET":
        return render_template("register.html")

    username = request.form["username"]
    password = request.form["password"]
    if sql_queries.register(username, password):
        return render_template("login_and_register.html")
    return render_template("error.html", message= f"This username already exists: {username}")


# sovelluksen tilan alustaminen testejä varten
@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    """Reset database for testing purposes."""
    user_repository.delete_all()
    return "Reset"


@app.route("/new_reference", methods=['GET', 'POST'])
def new_reference():
    """Render form with correct fields."""
    selected_type = request.form.get('ra', 'Article')
    return render_template("form.html", selected_type=selected_type)



