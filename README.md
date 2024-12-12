# Task Manager Django Web Application

## Overview
This is a simple task manager web application built using the Django framework. The application allows users to sign up, log in, log out, and manage their tasks efficiently. Users can create, update, delete, and search tasks through a responsive and intuitive interface.

---

## Features
1. **User Management:**
   - Sign-up functionality for new users.
   - Secure login and logout features.
2. **Task Management:**
   - Create, view, update, and delete tasks.
   - Search tasks by title using a search bar.
3. **Responsive Design:**
   - HTML templates styled for responsive layouts.
4. **Database Integration:**
   - Uses SQLite for persistent data storage.

---

## Application Structure
```
project_root/
    user_management_project/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    core/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        tests.py
        urls.py
        views.py
        templates/
            core/
                base.html
                signup.html
                login.html
                task_list.html
                task_form.html
                task_confirm_delete.html
    db.sqlite3  # SQLite database
    manage.py
```

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd project_root
   ```

2. **Install Dependencies:**
   Ensure you have Django installed. If not, run:
   ```bash
   pip install django
   ```

3. **Apply Migrations:**
   Set up the database by running:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Server:**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Usage Instructions
1. **Sign Up:**
   - Go to `/signup/` and create a new user account.
2. **Log In:**
   - Use your credentials to log in at `/login/`.
3. **Manage Tasks:**
   - Create new tasks using the "New Task" button on the homepage.
   - Edit or delete tasks directly from the task list.
4. **Search Tasks:**
   - Use the search bar to filter tasks by title.

---

## Project Design
1. **Backend:**
   - Built with Django, utilizing its built-in authentication system and ORM for database management.
2. **Frontend:**
   - HTML templates with optional Bootstrap integration for styling and responsiveness.
3. **Database:**
   - SQLite is used for persistent data storage, managed through Django’s ORM.

---

## Known Issues and Future Enhancements
1. **Known Issues:**
   - None reported.
2. **Future Enhancements:**
   - Add task prioritization and due dates.
   - Improve styling with a more modern CSS framework.

---

## License
This project is for educational purposes and is not licensed for commercial use.

---

## Contact
For any questions or issues, please contact [Your Email Address or GitHub Profile].



