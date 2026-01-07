import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert a test user
cursor.execute(
    "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
    ("khushi", "1234")
)

conn.commit()
conn.close()

print("Database created with test user.")
