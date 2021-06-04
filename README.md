# web1_django
<<<<<<< HEAD
web project with Django

https://piwero-django1.herokuapp.com

web project for a company with a blog, contact form, services catalogue and shop.

## Getting started:

### Create and activate virtualenv
```commandline
virtualenv .venv -p python3
. .venv/bin/activate
<<<<<<< HEAD
or python3 -m virtualenv .venv
```

### Install requirements
```commandline
pip install Poetry
poetry install
```

#### Create basic local settings
```commandline
touch backend/core/settings/local.py
```

**local.py**:
```
from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ["*"]

```

### Secret keys
```commandline
touch .env
```

**.env**:
```
# Django secret
SECRET_KEY = ""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER = "" # Your Gmail 
EMAIL_HOST_PASSWORD = "" # Your Gmail password

Ask someone in the team to share their .env file with you, which contains the secrets of
the project. These secrets should never be pushed to the repository!

### Activate pre-commit configuration
```commandline
pre-commit install
```

### Migrate database
```commandline
python manage.py migrate
```

### Load fixtures
```commandline
python manage.py loaddata fixtures
```

### Run server

#### Run Web
```commandline
python manage.py runserver
```

http://localhost:8000/

