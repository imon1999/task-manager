# Task Manager Web Application

## Description

This is a web-based Task Manager application built using Python, FastAPI, Jinja2, and SQLAlchemy. It provides a simple and intuitive interface to manage your tasks efficiently.  You can add, edit, mark as complete, and delete tasks.

## Features

* **Add Tasks:** Easily add new tasks to your list.
* **View Tasks:** Displays all tasks, showing their completion status.
* **Mark as Complete:** Toggle tasks between complete and incomplete.
* **Edit Tasks:** Modify existing tasks.
* **Delete Tasks:** Remove tasks that are no longer needed.


## Technologies Used

* **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) 
* **Templating Engine:** [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) 
* **Database:** [SQLite](https://www.sqlite.org/index.html) 
* **ORM (Object-Relational Mapper):** [SQLAlchemy](https://www.sqlalchemy.org/) 
* **Frontend:** HTML, CSS
* **Web Server:** [Uvicorn](https://www.uvicorn.org/)
 
1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd task-manager
    ```


2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Access the Application:**
    Open your web browser and go to `http://localhost:8000`.



## Database

The application uses an SQLite database (`./sql_app.db` by default). The database file will be created automatically in the project directory when the application is run for the first time.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.
