from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Task(Base):
    """
    SQLAlchemy model for storing tasks in the database
    """
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)