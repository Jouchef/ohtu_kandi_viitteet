import sqlite3


def citate_to_db(self, author, title, book_title, journal, year, volume, pages, publisher):
    sql = "INSERT INTO citate (author, title, book_title, journal, year, volume, pages, publisher) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    data = (author, title, book_title, journal, year, volume, pages, publisher)
    self.cursor.execute(sql, data)
    self.conn.commit()
    return
