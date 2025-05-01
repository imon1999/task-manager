from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
import database
from pathlib import Path

# Create FastAPI application
app = FastAPI(title="Task Manager")

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get a database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to display the home page with all tasks
@app.get("/", response_class=HTMLResponse)
def read_tasks(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

# Route to add a new task
@app.post("/add")
def add_task(title: str = Form(...), db: Session = Depends(get_db)):
    task = models.Task(title=title, completed=False)
    db.add(task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

# Route to toggle task completion status via checkbox
@app.post("/toggle/{task_id}")
def toggle_complete_task(task_id: int, completed: bool = Form(False), db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = completed
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/edit/{task_id}", response_class=HTMLResponse)
def edit_task_form(request: Request, task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return templates.TemplateResponse("edit_task.html", {"request": request, "task": task})

@app.post("/update/{task_id}")
def update_task(task_id: int, title: str = Form(...), db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = title
    db.commit()
    return RedirectResponse(url="/", status_code=303)

# Route to delete a task
@app.get("/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)