

# Student Management System

This project is a Django-based application for managing student and teacher data, designed to facilitate CRUD operations and provide various analytics related to student performance.

## Features

- **Student Management:** Create, read, update, and delete student records.
- **Teacher Management:** Manage teacher details associated with students.
- **Analytics:** Retrieve top-performing students, filter by cutoff marks, passing status, and average marks.
- **RESTful API:** Fully functional REST API for frontend integration or external use.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8 or later:** Download from [python.org](https://www.python.org/downloads/).
- **Django 5.1.2:** Framework for building the application.
- **Django Rest Framework:** For building APIs.
- **Django Extensions:** For additional management commands.
- **SQLite (default):** For database management, included with Django.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/manuhari05/Student.git
   cd Student
   ```

2. **Create a Virtual Environment:**
   It is recommended to use a virtual environment to manage your project's dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**
   Make sure you have a `requirements.txt` file. If not, create one with the necessary packages:
   ```
   Django==5.1.2
   djangorestframework
   django-extensions
   ```
   Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   Apply the database migrations to set up the initial database structure.
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**
   (Optional) If you want to access the Django admin interface, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   Start the Django development server to test your application.
   ```bash
   python manage.py runserver
   ```
   Your application will be accessible at `http://127.0.0.1:8000/`.

## Using Django Extensions

To utilize additional features provided by Django Extensions, ensure it's included in your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_extensions',
]
```

### Commonly Used Commands

- **Graph Models:** Create visual representations of your models.
   ```bash
   python manage.py graph_models -a -o my_project_visualization.png
   ```
- **Open Shell:** Access Django's interactive shell with all models loaded.
   ```bash
   python manage.py shell_plus
   ```

## API Endpoints

### Students

- **List all students:** 
  - **Method:** `GET`
  - **Endpoint:** `/students/`
  - **Description:** Retrieve a list of all students.

- **Retrieve a student by roll number:** 
  - **Method:** `GET`
  - **Endpoint:** `/students/<rollno>/`
  - **Description:** Retrieve detailed information for a specific student.

- **Create a new student:** 
  - **Method:** `POST`
  - **Endpoint:** `/students/`
  - **Description:** Add a new student record. Requires student data in the request body.

- **Update a student:** 
  - **Method:** `PUT`
  - **Endpoint:** `/students/<rollno>/`
  - **Description:** Replace the entire student record.

- **Partially update a student:** 
  - **Method:** `PATCH`
  - **Endpoint:** `/students/<rollno>/`
  - **Description:** Update specific fields of a student record.

- **Delete a student:** 
  - **Method:** `DELETE`
  - **Endpoint:** `/students/<rollno>/`
  - **Description:** Remove a student record.

### Analytics

- **Get top students:** 
  - **Method:** `GET`
  - **Endpoint:** `/students/top/`
  - **Description:** Retrieve the top 5 students based on total marks.

- **Filter students by cutoff:** 
  - **Method:** `GET`
  - **Endpoint:** `/students/have/<cutoff>/`
  - **Description:** Retrieve students with marks above or below a specific cutoff.

- **Filter students by pass/fail status:** 
  - **Method:** `GET`
  - **Endpoint:** `/students/pass/<spass>/`
  - **Description:** Get students who passed or failed.

- **Filter students by average marks:** 
  - **Method:** `GET`
  - **Endpoint:** `/students/avg/<avg>/`
  - **Description:** Get students with marks above or below the average.

## Project Structure

```
Student/
│
├── MyApp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
|   |── utils.py
│   └── views.py
│
├── Student/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

<!-- ## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. -->

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used.
- [Django Rest Framework](https://www.django-rest-framework.org/) - For building the API.
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/) - For additional utilities.

