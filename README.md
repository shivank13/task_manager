# Task Management API

## Overview

A Django-based RESTful API for managing tasks, including creation, assignment, and task retrieval based on users.

## Features

- Create tasks
- Assign tasks to users
- Retrieve tasks assigned to specific users

## Requirements

- Python 3.x
- Django
- Django Rest Framework

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shivank13/task_manager.git
   cd task-manager

2. **Create a virtual environment and activate it:**
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. **Install dependencies:**
    pip install -r requirements.txt

4. **Run migrations:**
    python manage.py makemigrations
    python manage.py migrate

5. **Create a superuser:**
    python manage.py createsuperuser

6. **Start the development server:**
    python manage.py runserver

7. **Access the admin interface:**
    Go to http://127.0.0.1:8000/admin/
    Log in using your superuser credentials.

## API Endpoints

**Create Task:**

URL: api/tasks/create/
Method: POST
Body:
{
    "name": "Task 1",
    "description": "Complete the documentation",
    "task_type":"Dev",
    "status":"pending"
}
Response: 201 Created    
{
    "id": 4,
    "users": [],
    "name": "Task 1",
    "description": "Complete the documentation",
    "created_at": "2025-03-26T11:22:42.410958Z",
    "task_type": "Dev",
    "completed_at": null,
    "status": "pending"
}

**Assign Task:**

URL: api/tasks/<int:pk>/assign/
Method: POST
Body:
{
    "users": [1, 2]
}
Response: 200 OK
{"status":"users assigned"}

**Get User Tasks:**

URL: api/tasks/user/<int:user_id>/
Method: GET
Response: 200 OK
[
    {
        "id": 1,
        "name": "Task 1",
        "description": "Description here",
        ...
    }
]



## Test Credentials

Use the superuser for testing in the admin interface.
Create regular users via admin for testing task assignments.