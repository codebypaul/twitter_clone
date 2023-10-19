# Twitter Clone

## Project Design

###### Dependencies
- django
- django_rest_framework
- django_cors_headers
- python_dotenv

## Follow these steps to create the project
Create a directory for this project to live in
```console
mkdir <dir_name>
```

Enter into that newly created directory
```console
cd <dir_name>
```

Create a virtual environment
```console
python3 -m venv env
```

Activate your virtual environment
```console
source env/bin/activate
```

Install the dependencies/ packages
```console
pip3 django python_dotenv
```

Begin a Django project
```console
django-admin startproject <project_name>
```

Add other project files
```console
touch README.md .env .gitignore requirements.txt
```
#### Setting up auxilary files
Within the ```.env``` file we need to set up the following environment variables

```
DJANGO_SECRET_KEY = 
DB_NAME =
DB_USER =
DB_PASSWORD =
DB_PORT =
DB_HOST = 
```

To add all the required information for our ```.gitignore``` file, you will need to go to [copy and paste this template](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/).

Your ```requirements.txt``` file is extremely important because the environment folder (```env/```) will not be uploaded into your github repository due to our ```.gitignore```. All the dependencies/ packages need to be listed in this file so that you or anyone else may be able to install them when recreating or working on this project on another machine.

### Set up the project
Enter into newly created Django project
```console
cd <project_name>
```

It is time to set up the environment variables, first we will need to import the correct modules into our ```settings.py``` file. We will be importing **os and load_dotenv**.
```python
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
```
After importing the **load_dotenv** module we will need to call the **load_dotenv()** function.

Now that we have 


At this point it is time to decide which backend database you will use, Django comes with SQLite built in. My preference is PostgresQL, other options include:
- MariaDB
- Oracle
- MySQL

### SQLite
To use **SQLite** nothing needs to be done just run the following commands:
```console
python3 manage.yp makemigrations
python3 manage.py migrate
```

### PostgresQL
**Prerequisites**

**Package/ Depenencies**
- psycopg2_binary

Open the ```settings.py ``` file and scroll to the databases section. The database currently set up is SQLite you will see the following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

We will need to update the default database to show the following:
```python
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': os.environ.get('DB_NAME'),

        'USER': os.environ.get('DB_USER'),

        'PASSWORD': os.environ.get('DB_PASSWORD'),

        'HOST': os.environ.get('DB_HOST'),

        'PORT': os.environ.get('DB_PORT'),

    }
}
```

### MySQL
**Prerequisites**

**Package/ Depenencies**

```python
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'my_database',  
        'USER': 'root',  
        'PASSWORD': 'your_password',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}  
```

### MariaDB
**Prerequisites**

**Package/ Depenencies**
```python
DATABASES = {
    ‘default’: {
    ‘ENGINE’: ‘django.db.backends.mysql’,
    ‘NAME’: ‘myproject’,
    ‘USER’:’yourusername’,
    ‘PASSWORD’:’yourpassword',
    ‘HOST’:’localhost’,
    ‘PORT’:’’,
    }
}
```

<!-- ###### Oracle

```python

``` -->



