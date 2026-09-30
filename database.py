import sqlite3
from db_path import database_path

def create_users_table():

    conn = sqlite3.connect(database_path)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password)
        VALUES ('admin', '1234')
    """)

    conn.commit()
    conn.close()

connection = sqlite3.connect(database_path)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_no TEXT UNIQUE,
    name TEXT NOT NULL,
    father_name TEXT,
    class_name TEXT,
    section TEXT,
    phone TEXT,
    address TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_no TEXT,
    tuition_fee REAL,
    bus_fee REAL,
    total_fee REAL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_no TEXT,
    maths REAL,
    science REAL,
    english REAL
)
""")
connection.commit()
connection.close()

print("Database created successfully!")

if __name__ == "__main__":
    create_users_table()