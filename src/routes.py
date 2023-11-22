from app import app
from flask import Flask, render_template, redirect, request
import sql_queries


@app.route("/")
def index():
    """Render index"""
    return render_template("index.html")


@app.route("/new_reference")
def new_reference():
    """Render form."""
    return render_template("form.html")


@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    """Render form."""
    author = request.form["name"]
    title = request.form["title"]
    book_title = request.form["book_title"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volme"]
    pages = request.form["pages"]
    publisher = request.form["publisher"]
    sql_queries.citate_to_db(
        author, title, book_title, journal, year, volume, pages, publisher)
    return render_template("index.html", author=author, title=title, book_title=book_title, journal=journal, year=year, volume=volume, pages=pages, publisher=publisher)


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
    pass
