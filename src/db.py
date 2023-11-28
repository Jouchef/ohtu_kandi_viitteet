from os import getenv
from sqlalchemy import sql
from sqlalchemy.sql.elements import Null
from app import app
from flask_sqlalchemy import SQLAlchemy


# Initialize the SQLAlchemy object without directly associating it with the app
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
db = SQLAlchemy(app)
