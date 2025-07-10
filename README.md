#  User Management System - Django Project
A simple and powerful *Django-based User Management System* that supports registration, login/logout, profile management, password change, and an admin panel. It was built as part of a personal learning challenge.

##  Features

-  User Registration
-  Login & Logout
-  Profile View & Edit
-  Password Change
-  Admin Panel for User Management
-  Custom User Types (Staff & Community Members)
-  Authentication-protected profile page
-  Unit Tests for Models and Views


##  Tech Stack
- **Backend**: Django 5.2
- **Database**: SQLite
- **Frontend**: HTML, CSS (basic)


## 📸 Screenshots

> 🖼 Add screenshots of:

![Screenshot (24)](https://github.com/user-attachments/assets/8e2dc372-ce82-4522-9533-3b0c04b16ff1)

![Screenshot (23)](https://github.com/user-attachments/assets/25aa786b-adcc-4365-9c89-4d1dcb80ea30)

 ![Screenshot (22)](https://github.com/user-attachments/assets/783babcc-5ebb-4ac9-b55b-00479a842b0a)



##  Setup Instructions

### 1. Create and activate virtual environment
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


