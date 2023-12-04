"""Data model for a reference.
    Using SQLAlchemy ORM. """

from db import db # pylint: disable=import-error no-name-in-module

class Reference_model(db.Model): # pylint: disable=invalid-name too-few-public-methods
    """Reference class definition."""
    __tablename__ = "references_table"

    id = db.Column(db.Integer, primary_key=True)
    reference_type = db.Column(db.Text, nullable=True)
    visible = db.Column(db.Boolean, default=True, nullable=True)
    author = db.Column(db.Text, nullable=True)
    title = db.Column(db.Text, nullable=True)
    journal = db.Column(db.Text, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    volume = db.Column(db.Integer, nullable=True)
    publisher = db.Column(db.Text, nullable=True)
    booktitle = db.Column(db.Text, nullable=True)
    number = db.Column(db.Text, nullable=True)
    pages = db.Column(db.Text, nullable=True)
    month = db.Column(db.Integer, nullable=True)
    doi = db.Column(db.Text, nullable=True)
    note = db.Column(db.Text, nullable=True)
    key = db.Column(db.Text, nullable=True)
    series = db.Column(db.Text, nullable=True)
    address = db.Column(db.Text, nullable=True)
    edition = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=True)
    editor = db.Column(db.Text, nullable=True)
    organization = db.Column(db.Text, nullable=True)
