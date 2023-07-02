import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

connection.commit()
connection.close()