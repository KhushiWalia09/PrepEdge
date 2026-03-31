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
    ("HR", "Describe a time when you had to overcome a significant challenge."),
    ("HR", "Where do you see yourself in five years?"),
    ("HR", "What is your proudest professional achievement?"),
    ("HR", "Why do you want to work for this company specifically?"),
    ("HR", "How do you handle conflicts within a team?"),
    ("Technical", "What is Python?"),
    ("Technical", "Difference between list and tuple."),
    ("Technical", "What is Flask?"),
    ("Technical", "Explain the differences between REST and GraphQL."),
    ("Technical", "What are the main principles of Object-Oriented Programming (OOP)?"),
    ("Technical", "Explain the concept of closures in JavaScript."),
    ("Technical", "What is the purpose of a database index and how does it work?"),
    ("Technical", "Describe the differences between SQL and NoSQL databases.")
]

cursor.executemany(
    "INSERT INTO questions (category, question) VALUES (?, ?)",
    sample_questions
)

conn.commit()
conn.close()

print("Questions table created and populated.")
