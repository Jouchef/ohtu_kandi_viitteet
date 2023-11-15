from app import app
from flask import Flask, render_template, redirect

@app.route("/")
def index():
    return render_template("index.html")

