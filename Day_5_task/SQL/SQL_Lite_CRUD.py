import sqlite3

## creating database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# ## Creating table
# cursor.execute("""
# CREATE TABLE students(
# id INTEGER PRIMARY KEY,
# name TEXT,
# age INTEGER
# )
# """)

## insert values in the table
cursor.execute("INSERT INTO students VALUES (1,'Manoj',21)")
cursor.execute("INSERT INTO students VALUES (2,'Muhesh',22)")
cursor.execute("INSERT INTO students VALUES (3,'chandru',23)")
cursor.execute("INSERT INTO students VALUES (4,'Ananth',24)")

## read values from the table
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

## update the student detail in the table
cursor.execute("UPDATE students SET age=27 WHERE id=1")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.execute("DELETE FROM students WHERE id=1")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())