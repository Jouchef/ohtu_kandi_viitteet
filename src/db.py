from os import getenv
from app import app
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object without directly associating it with the app
db = SQLAlchemy()
