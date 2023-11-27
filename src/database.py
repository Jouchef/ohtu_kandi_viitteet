from flask_sqlalchemy import SQLAlchemy
from os import getenv
from extensions import db, app

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://maija:risla47@localhost/ohtu'
db = SQLAlchemy(app)
