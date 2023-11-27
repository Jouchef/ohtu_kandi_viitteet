from flask_sqlalchemy import SQLAlchemy
from os import getenv
from extensions import db, app

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
