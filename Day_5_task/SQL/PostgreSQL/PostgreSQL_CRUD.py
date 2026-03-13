import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="school",
    user="postgres",
    password="mmmm",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Insert data
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Chandru", 23))

# Read data
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# Update data
cursor.execute("UPDATE students SET age = %s WHERE name = %s", (24, "Chandru"))
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# Delete data
cursor.execute("DELETE FROM students WHERE name = %s", ("Chandru",))
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.commit()
conn.close()