import sqlite3
import random
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "prepedgesupersecret"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            session["role"] = user[3]
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, password, "aspirant")
            )
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            error = "Username already exists"
    return render_template("signup.html", error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/mock")
def mock():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT question FROM questions")
    questions = cursor.fetchall()
    conn.close()

    if not questions:
        question = "No questions available yet."
    else:
        question = random.choice(questions)[0]

    return render_template("mock.html", question=question)

@app.route("/questions")
def questions():
    if "user" not in session:
        return redirect(url_for("login"))

    category = request.args.get("category")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if category:
        cursor.execute(
            "SELECT category, question FROM questions WHERE category=?",
            (category,)
        )
    else:
        cursor.execute("SELECT category, question FROM questions")

    questions = cursor.fetchall()
    conn.close()

    return render_template("questions.html", questions=questions, selected_category=category)

@app.route("/add-question", methods=["GET", "POST"])
def add_question():
    if "user" not in session or session.get("role") != "admin":
        return redirect(url_for("dashboard"))

    message = None

    if request.method == "POST":
        category = request.form["category"]
        question = request.form["question"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO questions (category, question) VALUES (?, ?)",
            (category, question)
        )

        conn.commit()
        conn.close()

        message = "Question added successfully!"

    return render_template("add_question.html", message=message)

@app.route("/progress")
def progress():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("progress.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("role", None)
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
