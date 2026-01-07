import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Add role column if not exists
cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'aspirant'")

# Make one admin user
cursor.execute(
    "UPDATE users SET role='admin' WHERE username='khushi'"
)

conn.commit()
conn.close()

print("Role column added and admin set.")
