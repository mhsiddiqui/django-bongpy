import datetime
import os

import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ")cqmpi+p@n&!u&fu@!m@9h&1bz9mwmstsahe)nf!ms+c$uc=x7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sessions',
    'bongpy',
    'tests',
]

MIDDLEWARE_CLASSES = [
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
]

MIDDLEWARE = MIDDLEWARE_CLASSES

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

BONGPY_DEFAULTS = {
    'BOOLEAN_KEY_DEFAULT': False,
    'INTEGER_KEY_DEFAULT': 5,
    'STRING_KEY_DEFAULT': 'string default',
    'DATE_KEY_DEFAULT': datetime.datetime.now().date(),
    'DATETIME_KEY_DEFAULT': datetime.datetime.now(),
    'TIME_KEY_DEFAULT': datetime.datetime.now().time(),
    'LIST_KEY_DEFAULT': [1, 2, 3],
    'DICT_KEY_DEFAULT': {"1": 1, "2": 2},
    'JSON_KEY_DEFAULT': {
        "a": [1, 2, 3],
        "b": {
            "a": 1
        }
    },
}
