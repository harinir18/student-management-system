# Student Management System

A full-stack Student Management System built with Python (Flask), MySQL, and vanilla HTML/CSS/JS.

## Features
- Full CRUD operations for managing students
- RESTful HTTP APIs built with Flask
- MySQL backend using PyMySQL
- Modern, clean, and responsive UI
- Client-side and server-side validation

## Database Setup

1. Make sure you have MySQL installed and running on your system.
2. Login to your MySQL server and create the required database:
```sql
CREATE DATABASE student_db;
```
*(Note: Our application will automatically create the `students` table when it starts up!)*
3. If necessary, update the MySQL credentials within `backend/db.py`:
Modify the `get_db_connection()` function if your local MySQL uses a different username/password. Default assumes `user='root'` and `password='password'`.

## Backend Setup

1. Open a terminal and navigate to the root directory `Student Management System`.
2. (Optional but recommended) Create a virtual environment:
```shell
python -m venv venv
venv\Scripts\activate       # On Windows
# source venv/bin/activate  # On macOS/Linux
```
3. Install the Python dependencies:
```shell
pip install -r requirements.txt
```
4. Start the backend server:
```shell
python backend/app.py
```
The server will run on `http://127.0.0.1:5000/`. Keep this terminal open!

## Frontend Setup

The frontend consists of standalone static HTML files.

1. Locate the `frontend` folder inside this project.
2. Double-click on `index.html` to open it in your web browser (or better yet, run a small local web server if you experience CORS issues, like using Live Server in VSCode or `python -m http.server 8000` inside the `frontend` directory).
3. The frontend will communicate automatically with the Flask backend running on port 5000 via our JavaScript APIs.

Navigate through the Dashboard to:
- View all students
- Add a new student
- Edit current students
- Delete students
