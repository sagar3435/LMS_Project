Library Management System

A Django REST Framework-based backend project that allows admins to manage books (CRUD) and students to view them. Authentication is token-based using JWT.


Setup Instructions

1. Clone the Repository

  git clone https://github.com/sagar3435/LMS_Project.git

  cd LMS_Project

2. Create & Activate a Virtual Environment

  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies

  pip install -r requirements.txt

4. Run Migrations

  python manage.py makemigrations
  python manage.py migrate

5. Run the Server
  python manage.py runserver
