import csv
from csv import reader
import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

with open('books2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row['title']
        author = row['author']
        year = int(row['year'])

        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", 
                       (title, author, year))
        
connection.commit()
connection.close()
    