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
    sql = text(
        "SELECT * FROM References_Table WHERE visible = 1 ORDER BY Author ASC")

    try:
        result = db.session.execute(sql)

        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None


def search_by_name_from_db():
    pass


def change_visible_to_false():
    sql = text("UPDATE References_Table SET visible = 0 WHERE id = :id")

    try:
        result = db.session.execute(sql, {"id": id})

        db.session.commit()

        return
    except Exception as e:
        db.session.rollback()
        return None


def edit_queries():
    pass
    # sql = text(
    #  "SELECT author, title, book_title, journal, year, volume, pages, publisher WHERE ")

    # haetaan listaan kaikki sitaatit


def ids_list():
    ids_list = []
    sql = text("SELECT id FROM references_table WHERE visible = TRUE")
    data = db.session.execute(sql)
    data = data.fetchall()
    for id in data:
        ids_list.append(id[0])
    return ids_list


def citates_to_list():
    citates_dict = {}
    print(ids_list())
    for idnex, id in enumerate(ids_list()):
        sql = text(
            "SELECT author, title, year, type FROM References_Table WHERE id = :id")
        result = db.session.execute(sql, {"id": id}).fetchall()
        for j in result:
            author, title, year, type = result
            citates_dict[id] = {
                'author': author,
                'title': title,
                'year': year,
                'type': type
            }
    print(citates_dict)
    return citates_dict
