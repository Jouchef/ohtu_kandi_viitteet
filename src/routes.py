from app import app
from flask import Flask, render_template, redirect, request
import save_citate_to_db


@app.route("/")
def index():
    """Render index"""
    return render_template("index.html")


@app.route("/new_reference")
def new_reference():
    """Render form."""
    return render_template("form.html")


@app.route("/add_reference", methods=["POST"])
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
    save_citate_to_db.citate_to_db(
        author, title, book_title, journal, year, volume, pages, publisher)
    return render_template("index.html")  # tässä takaisin etusivulle?
