"""User reference connecting model to database""" # pylint disable=invalid-name
from src.db import db # pylint: disable=import-error no-name-in-module


class UserReferences_model(db.Model): # pylint: disable=invalid-name too-few-public-methods
    """User references tables as database model.
    Has a table in the database with the name "UserReferences_Table".
    Each user reference has an id, user_id and reference_id.
    Connects users and references together."""

    __tablename__ = "userreferences_table"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users_table.id"))
    reference_id = db.Column(db.Integer, db.ForeignKey("references_table.id"))

    user = db.relationship('User_model', backref='user_references')
    reference = db.relationship('Reference_model', backref='reference_users')
