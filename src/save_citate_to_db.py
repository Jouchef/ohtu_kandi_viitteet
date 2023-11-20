import sqlite3
from sqlalchemy import text
from database import db


def citate_to_db(self, author, title, book_title, journal, year, volume, pages, publisher):
    sql = text("INSERT INTO References (author, title, booktitle, journal, year, volume, pages, publisher) VALUES (:self, author, title, book_title, journal, year, volume, pages, publisher)")

    try:
        result = db.session.execute(sql, {"author": author, "title": title, "booktitle": book_title,
                                    "journal": journal, "year": year, "volume": volume, "pages": pages, "publisher": publisher})
        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None
