from flask_sqlalchemy import SQLAlchemy
from app import app
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://maija:risla47@localhost/ohtu'
db = SQLAlchemy(app)
