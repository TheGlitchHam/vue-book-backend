import sqlite3


conn = sqlite3.connect('books.sqlite ')
cursor = conn.cursor()


def init_db():
    try:
        sql_query = "CREATE TABLE book( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL, read BOOLEAN DEFAULT false)"
        cursor.execute(sql_query)
    except sqlite3.Error as error:
        print("Error executing init script", error)


def get_connection():
    return conn


def get_all_books():
    book_list = []
    try:
        cursor.execute("SELECT * FROM book")
        book_list.extend(cursor.fetchall())
    except sqlite3.Error as error:
        print("Error loading all books", error)
    return book_list


def get_book_by_id(bookID):
    book
    try:
        cursor.execute("SELECT * FROM book where id = ?", (bookID))
        book = cursor.fetchone()
    except sqlite3.Error as error:
        print("Error loading book", error)
    return book


def add_book_db(book):
    message
    try:
        cursor.execute(
            "INSERT INTO book(title, author, read) VALUES (?, ?, ?)", (book.get("title"), book.get("author"), book.get("read")))
        conn.commit()
        message = "Added book to Database"
    except sqlite3.Error as error:
        print("Error adding book", error)
        message = ("Error: could not add book")
    return message


def delete_book(bookID):
    message
    try:
        sql_query = "DELETE from book where id = ?"
        cursor.execute(sql_query, (bookID))
        conn.commit()
        message = "Deleted book successfully"
    except sqlite3.Error as error:
        print("Error delete book", error)
        message = ("Error: could not delete book")
    return message


def update_book(book):
    message
    try:
        sql_query = "UPDATE book SET title = ? , author = ? , read = ? WHERE id = ? "
        cursor.execute(sql_query, (book.get("title"),
                                   book.get("author"), book.get("read"), book.get("id")))
        conn.commit()
        message = "Successfully updated book"
    except sqlite3.Error as error:
        print("Error updating book", error)
        message = ("Error: could not update book")
    return message
