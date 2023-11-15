from app import app
from flask import Flask, render_template, redirect

@app.route("/")
def index():
    """Render index"""
    return render_template("index.html")

@app.route("/new_reference")
def new_reference():
    """Render form."""
    return render_template("form.html")