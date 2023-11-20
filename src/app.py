from flask import Flask
from os import getenv
from database import db
from os import environ
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL")

db.init_app(app)

import routes  # nopep8
