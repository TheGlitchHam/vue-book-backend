import sqlite3


conn = sqlite3.connect('books.sqlite ')
cursor = conn.cursor()


def init_db():
    sql_query = "CREATE TABLE book( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL, read BOOLEAN DEFAULT false)"
    cursor.execute(sql_query)


def get_connection():
    return conn


def get_all_books():
    pass


def get_book_by_id():
    pass


def add_book_db(book):
    curser.execute(
        "INSERT INTO book(title, author, read) VALUES (?, ?, ?)", (book.get("title"), book.get("author"), book.get("read")))
    return "success"


def delete_book(bookID):
    pass


def update_book(book):
    clearpass


def test_add_book():
    book = {"title": "testtitle", "author": "testauthor", "read": "false"}
    add_book_db(book)
