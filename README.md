# Doctor Appointment Booking System

This project is a Django-based booking system where users can book appointments with doctors. It utilizes a MySQL database to store information related to users, doctors, and bookings.

## Prerequisites

- **Python 3.x** installed on your system.
- **MySQL** installed and running.

##Notice

Please note that the project folder is getTicket. And other folders are apps that can be scaled in the future for users, doctors, and booking system.

## Setting Up the MySQL Database

1. **Create a new database** in MySQL:

   ```sql
   CREATE DATABASE doctorque_db;
    ```
2. Update the settings.py file in your Django project to include the MySQL database configurations:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'doctorque_db',
        'USER': 'root', 
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Install Requirements

1. Create a virtual environment (optional but recommended):

```
python -m venv venv
```

2. Activate the virtual environment:

```
venv\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Run Migrations:

Apply the migrations to set up your database schema:

```
python manage.py makemigrations
python manage.py migrate
```

## Run the Tests:

```
python manage.py test
```



