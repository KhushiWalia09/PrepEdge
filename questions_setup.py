import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    question TEXT NOT NULL
)
""")

# Sample questions
sample_questions = [
    ("HR", "Tell me about yourself."),
    ("HR", "What are your strengths and weaknesses?"),
    ("HR", "Why should we hire you?"),
    ("Technical", "What is Python?"),
    ("Technical", "Difference between list and tuple."),
    ("Technical", "What is Flask?")
]

cursor.executemany(
    "INSERT INTO questions (category, question) VALUES (?, ?)",
    sample_questions
)

conn.commit()
conn.close()

print("Questions table created and populated.")
