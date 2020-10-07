DROP TABLE IF EXISTS books;
CREATE TABLE post(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  read BOOLEAN DEFAULT false,
)