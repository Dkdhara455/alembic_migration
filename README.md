# FastAPI Project — PostgreSQL + Alembic Migration Setup

This project uses **FastAPI**, **SQLAlchemy**, **JWT Authentication**, and **Alembic** for database migrations.  
Originally it was configured with SQLite, and now it’s migrated to **PostgreSQL**.

---

## 📦 Prerequisites

- **Python 3.10+**
- **PostgreSQL installed** (with pgAdmin4 or psql CLI)
- Basic knowledge of FastAPI & SQLAlchemy

---

## ⚙️ 1. Install Dependencies

```bash
pip install psycopg2-binary alembic
Option 1: Using pgAdmin 4

Open pgAdmin 4.

Right-click Servers → Connect to your PostgreSQL instance.

Create a new database (e.g., mydb).

Check your username from Server → Properties → Connection tab (default: postgres).

Option 2: Using SQL

CREATE DATABASE mydb;

CREATE USER myuser WITH PASSWORD 'mypassword';

GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

database.py or your .env file replace the sqlite url with popstgresql 

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydb"

## intialize alembic

alembic init alembic

## create and apply migrations 

alembic revision --autogenerate -m "Initial migration"

alembic upgrade head

