# Task 1C – Backend CRUD Application (Flask + SQLite)

## Project Description
This project is a backend CRUD (Create, Read, Update, Delete) application developed using Python Flask and SQLite.
The application exposes RESTful API endpoints to create, read, update, and delete user data.
All APIs were tested using Postman and the backend is deployed on a public server (PythonAnywhere).

---
## Relevant Screenshots
https://drive.google.com/drive/folders/1L3HUVlXOgo3R3RG7RURvIyxc5OAT0JmI?usp=sharing

---
## Tools & Technologies Used
- Python
- Flask
- SQLite
- Postman
- PythonAnywhere

---

## Base URL
https://sanjeeth.pythonanywhere.com

---

## API Endpoint Documentation (CRUD)

### 1. Backend Status Check
**GET /**
Response:
{
  "message": "Task 1C Backend API is running",
  "endpoints": {
    "CREATE": "POST /users",
    "READ": "GET /users",
    "UPDATE": "PUT /users/<id>",
    "DELETE": "DELETE /users/<id>"
  }
}

---

### 2. CREATE – Add New User
**POST /users**
Headers:
Content-Type: application/json

Body:
{
  "name": "Alice",
  "email": "alice@gmail.com",
  "age": 20
}

Response:
{
  "message": "User added"
}

---

### 3. READ – Fetch All Users
**GET /users**
Response:
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@gmail.com",
    "age": 20
  }
]

---

### 4. UPDATE – Modify Existing User
**PUT /users/{id}**
Headers:
Content-Type: application/json

Body:
{
  "name": "Alice Updated",
  "email": "alice_updated@gmail.com",
  "age": 21
}

Response:
{
  "message": "User updated"
}

---

### 5. DELETE – Remove User
**DELETE /users/{id}**
Response:
{
  "message": "User deleted"
}

---

## How to Run Locally
pip install -r requirements.txt
python app.py

---

## Deployment
The backend is deployed on PythonAnywhere and is publicly accessible.

---

## Conclusion
This project demonstrates backend development using Flask with full CRUD functionality, SQLite database integration, REST API design, testing using Postman, and deployment on a public server.
