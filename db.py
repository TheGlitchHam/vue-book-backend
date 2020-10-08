import sqlite3


conn = sqlite3.connect('books.sqlite ')
cursor = conn.cursor()


def init_db():
    sql_query = "CREATE TABLE book( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL, read BOOLEAN DEFAULT false)"
    cursor.execute(sql_query)


def get_connection():
    return conn


def get_all_books():
    cursor.execute("SELECT * FROM book")
    book_list = cursor.fetchall()
    return book_list


def get_book_by_id(bookID):
    cursor.execute("SELECT * FROM book where id = ?", (bookID))
    book = cursor.fetchone()
    return book


def add_book_db(book):
    cursor.execute(
        "INSERT INTO book(title, author, read) VALUES (?, ?, ?)", (book.get("title"), book.get("author"), book.get("read")))
    conn.commit()
    return "Added book to Database"


def delete_book(bookID):
    sql_query = "DELETE from book where id = ?"
    cursor.execute(sql_query, (bookID))
    conn.commit()
    return "Book deleted Successfully"


def update_book(book):
    sql_query = "UPDATE book SET title = ? , author = ? , read = ? WHERE id = ? "
    cursor.execute(sql_query, (book.get("title"),
                               book.get("author"), book.get("read"), book.get("id")))
    conn.commit()
    return "Successfully updated book"


def test_book():
    book = {"title": "dinges", "author": "testauth", "read": "True", "id": "1"}

    print(update_book(book))
    print(get_all_books())
