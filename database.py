from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a SQLite database URL
DATABASE_URL = "sqlite:///./tasks.db"

# Create the database engine with check_same_thread=False for SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class
SessionLocal = sessionmaker(bind=engine)

# Create a Base class for our models
Base = declarative_base()