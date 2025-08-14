from fastapi import FastAPI
from main_project.routes import user
from main_project.db.database import Base, engine

# Create tables if not using Alembic yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI PostgreSQL JWT Project")

# Include routes
app.include_router(user.router)

