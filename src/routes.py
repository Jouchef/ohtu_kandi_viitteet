"""Main module for the application."""

from repositories.user_repository import user_repository
from services.user_service import user_service
import sql_queries
from sql_queries import change_visible_to_false
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app
from db import db
import psycopg2
import os
from dotenv import load_dotenv


# Define the Reference model
class Reference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    journal = db.Column(db.String(100))
    year = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    number = db.Column(db.Integer)
    pages = db.Column(db.String(100))
    month = db.Column(db.String(100))
    doi = db.Column(db.String(100))
    note = db.Column(db.String(100))
    key = db.Column(db.String(100))

    def __init__(self, author, title, journal, year, volume, number, pages, month, doi, note, key):
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month
        self.doi = doi
        self.note = note
        self.key = key

# Define the routes
@app.route("/")
def render_home():
    references = Reference.query.all()
    return render_template('index.html', citates=references)

@app.route('/delete_reference/<int:citate_id>', methods=['POST'])
def delete_reference(citate_id):
    reference = Reference.query.get(citate_id)
    if reference:
        db.session.delete(reference)
        db.session.commit()
    return redirect(url_for("render_home"))

@app.route("/form", methods=["GET","POST"])
def add_reference():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
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

        reference = Reference(author=author, title=title, journal=journal, year=year, volume=volume, number=number,
                              pages=pages, month=month, doi=doi, note=note, key=key)
        db.session.add(reference)
        db.session.commit()

        return redirect(url_for("render_home"))





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



