# 🗄️ SQLAlchemy Student Management

A Python student management project built with **SQLAlchemy ORM** and **SQLite**, demonstrating relational database modeling and different types of relationships between students, fields, classrooms, and masters.

## ✨ Features

* 👨‍🎓 Student management
* 📚 Field management
* 🏫 Classroom management
* 👨‍🏫 Master management
* 🔗 One-to-many relationships
* 🔄 Many-to-many relationships
* 🔑 Primary and foreign keys
* 💾 SQLite database
* 🧩 SQLAlchemy ORM models
* 🛠️ Modern SQLAlchemy 2.x syntax

## 🛠️ Tech Stack

* **Python 3**
* **SQLAlchemy 2.x**
* **SQLite**
* **SQLAlchemy ORM**

## 🏗️ Database Structure

The project models the following relationships:

```text
Field
├── Students
└── Classrooms

Master
└── Classrooms

Student
└── Classrooms (many-to-many)
```

The many-to-many relationship between students and classrooms is implemented using an association table:

```text
Student
   │
   │
   ▼
student_classroom
   ▲
   │
   │
ClassRoom
```

## 📁 Project Structure

```text
sqlalchemy-student-management/
│
├── database.py
├── main.py
├── mydatabase.db
└── README.md
```

### `database.py`

Contains:

* SQLAlchemy declarative base
* ORM models
* Database relationships
* Association table
* Database engine and session management

### `main.py`

Demonstrates:

* Creating database records
* Connecting related models
* Adding students to classrooms
* Committing changes
* Querying and displaying objects

## 🚀 Getting Started

### 1. Install SQLAlchemy

```bash
pip install sqlalchemy
```

### 2. Run the project

```bash
python main.py
```

The SQLite database is created automatically when the application starts.

## 🧠 What I Explored

* SQLAlchemy ORM
* Declarative models
* SQLAlchemy 2.x typed mappings
* Primary and foreign keys
* One-to-many relationships
* Many-to-many relationships
* Association tables
* Sessions and transactions
* SQLite database integration
* Separating database models from application logic

## 🔮 Future Improvements

* Add CRUD operations for all models
* Add Alembic database migrations
* Add repository/service layers
* Add input validation
* Add automated tests
* Replace SQLite with PostgreSQL

---

**Built by ARK13** — a hands-on SQLAlchemy project exploring ORM design, relational databases, and model relationships.
