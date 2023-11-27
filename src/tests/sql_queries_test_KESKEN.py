
import unittest
from sql_queries import article_to_db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from os import getenv

class TestSqlQueries(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
        self.db = SQLAlchemy(app)

    def test_article_to_db(self):
        author = "John Doe"
        title = "Sample Article"
        journal = "Sample Journal"
        year = 2022
        volume = 1
        number = 1
        pages = "1-10"
        month = "January"
        doi = "10.1234/sample"
        note = "Sample note"
        key = "sample-key"

        article_to_db(author, title, journal, year, volume, number, pages, month, doi, note, key, self.db)
        sql = text("SELECT * FROM References_Table WHERE title=:title")
        query = self.db.session.execute(sql, {"title": title})
        row = query.fetchone()

        self.assertEqual(row.author, author)
        self.assertEqual(row.journal, journal)
        self.assertEqual(row.year, year)
        self.assertEqual(row.volume, volume)
        self.assertEqual(row.number, number)
        self.assertEqual(row.pages, pages)
        self.assertEqual(row.month, month)
        self.assertEqual(row.doi, doi)
        self.assertEqual(row.note, note)
        self.assertEqual(row.key, key)
