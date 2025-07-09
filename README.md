#  Django User Management System

A simple Django project for managing user accounts with features like registration, login/logout, profile editing, password change, and an admin dashboard.

## Features

-  User Registration & Login
-  User Authentication (with mock verification)
-  Profile Management (view, edit, upload profile picture)
-  Password Change
-  Admin Panel (view & manage all users)
-  Unit Tests for models and views


##  Tech Stack

- **Backend**: Django 5.2
- **Database**: SQLite
- **Frontend**: HTML, CSS (basic)


##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/django-user-management.git
cd django-user-management
2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py migrate
5. Start the server
python manage.py runserver
Open your browser at http://127.0.0.1:8000

 Admin Access
To access the Django Admin panel:

python manage.py createsuperuser
Then login at http://127.0.0.1:8000/admin

 Run Tests
python manage.py test
Screenshots

!(https://github.com/user-attachments/assets/edbdae12-8b65-424d-9cad-d3583f930a18)


!(https://github.com/user-attachments/assets/8f74705b-6190-43fc-8e4b-7c685d52fb9a)

!(https://github.com/user-attachments/assets/04bf14cf-77e6-41a6-a35c-7538a720eaa7)



 Deployment
Add your live site link here if deployed.

 Author
Malicha Galma
Student Developer, July 2025

