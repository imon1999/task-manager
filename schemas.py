"""
Defines Pydantic schemas for data validation and transfer
related to tasks in the Task Manager application.
"""
from pydantic import BaseModel

class TaskBase(BaseModel):
    """Base schema with common attributes"""
    title: str

class TaskCreate(TaskBase):
    """Schema for creating tasks (inherits title from TaskBase)"""
    pass

class Task(TaskBase):
    """Schema for returning tasks (includes all fields from the database)"""
    id: int
    completed: bool

    class Config:
        """Configure ORM mode for Pydantic to work with SQLAlchemy"""
        orm_mode = True