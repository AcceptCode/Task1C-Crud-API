from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return jsonify({
        "message": "Task 1C Backend API is running",
        "endpoints": {
            "POST": "/users",
            "GET": "/users",
            "PUT": "/users/<id>",
            "DELETE": "/users/<id>"
        }
    })

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    conn = get_db()
    conn.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        (data["name"], data["email"], data["age"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "User added"})

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    conn = get_db()
    conn.execute(
        "UPDATE users SET name=?, email=?, age=? WHERE id=?",
        (data["name"], data["email"], data["age"], id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated"})

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
