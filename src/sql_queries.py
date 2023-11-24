import sqlite3
from sqlalchemy import text
from database import db
"""This file contains all the SQL queries that are used in the application.
"""

# NOT IN USE !!
# Will be replaced byt article_to_db(), book_to_db() and inproceedings_to_db().
def citate_to_db(author, title, book_title, journal, year, volume, pages, publisher):
    sql = text("INSERT INTO References_Table (author, title, booktitle, journal, year, volume, pages, publisher) VALUES (:author, :title, :booktitle, :journal, :year, :volume, :pages, :publisher)")

    try:
        result = db.session.execute(sql, {"author": author, "title": title, "booktitle": book_title,
                                    "journal": journal, "year": year, "volume": volume, "pages": pages, "publisher": publisher})
        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None

def article_to_db(author, title, journal, year, volume, number=None,
                   pages=None, month=None, doi=None, note=None, key=None):
    sql = text("INSERT INTO References_Table (type, visible, author, title, journal, year, volume, number, pages, month, doi, note, key)"
               " VALUES (:author, :title, :journal, :year, :volume, :number, :pages, :month, :doi, :note, :key)")
    
    try:
        result = db.session.execute(sql, {"type": "article", "visible": 1, "author": author,
                                          "title": title, "journal": journal, "year": year, "volume": volume,
                                          "number": number, "pages": pages, "month": month, "doi": doi,
                                          "note": note, "key": key})

        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None

def book_to_db():
    pass

def inproceedings_to_db():
    pass

def all_references_from_db():
    sql = text("SELECT * FROM References_Table WHERE visible = 1 ORDER BY author ASC")

    try:
        result = db.session.execute(sql)

        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None


def search_by_name_from_db(search):
    sql = text("SELECT * FROM References_Table WHERE visible = 1 AND LOWER(author) LIKE LOWER(:author) ORDER BY author ASC")

    try:
        result = db.session.execute(sql, {"author": f"%{search}%"}).fetchall()

        db.session.commit()

        return result

    except Exception as e:
        db.session.rollback()
        return None

def change_visible_to_false():
    sql = text("UPDATE References_Table SET visible = 0 WHERE id = :id")

    try:
        result = db.session.execute(sql, {"id": id})

        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None

def edit_queries(author, title, booktitle, journal, year, volume, pages, publisher, id):
    sql = text("UPDATE References_Table SET"
               " author = COALESCE(:author, author),"
               " title = COALESCE(:title, title),"
               " booktitle = COALESCE(:booktitle, booktitle),"
               " journal = COALESCE(:journal, journal),"
               " year = COALESCE(:year, year),"
               " volume = COALESCE(:volume, volume),"
               " pages = COALESCE(:pages, pages),"
               " publisher = COALESCE(:publisher, publisher)"
               " WHERE id = :id")

    try:
        result = db.session.execute(sql, {"author": author, "title": title, "booktitle": booktitle,
                                           "journal": journal, "year": year, "volume": volume,
                                           "pages": pages, "publisher": publisher, "id": id})

        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None
