"""Database model for user entity.
    Using SQLAlchemy ORM. """
from src.db import db # pylint: disable=import-error no-name-in-module

class User_model(db.Model): # pylint: disable=invalid-name too-few-public-methods
    """User class definition.
    Has a table in the database with the name "Users_Table".
    Each user has an id, username and password."""
    __tablename__ = "users_table"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
