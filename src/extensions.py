from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import getenv
db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL") # this is retrieved from the .env file