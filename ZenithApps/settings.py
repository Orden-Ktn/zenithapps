from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY

SECRET_KEY = 'django-insecure-xxxxxxxx'

DEBUG = False

ALLOWED_HOSTS = [
    'zenithapps.pythonanywhere.com',
]


# APPLICATIONS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DeviZio',
    'LandInfo',
    'SkyView',
    'VorteKey',
    'PharmaBenin',
    'Depenso',
    'home',
]


# MIDDLEWARE

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",   # ← sessions
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",              # ← CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",   # ← messages
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLS

ROOT_URLCONF = 'ZenithApps.urls'


# TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / "templates"
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # dossier templates global
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",      # ← user dans templates
                "django.contrib.messages.context_processors.messages",  # ← messages
            ],
        },
    },
]


# WSGI

WSGI_APPLICATION = 'ZenithApps.wsgi.application'


# DATABASE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


LOGIN_URL          = "/connexion/"      # redirigé ici si @login_required
LOGIN_REDIRECT_URL = "/"               # après connexion réussie sans "next"
LOGOUT_REDIRECT_URL = "/connexion/"   # après déconnexion
 

# PASSWORD VALIDATION

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# LANGUAGE

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# STATIC FILES

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# DEFAULT PRIMARY KEY

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 3600 secondes = 1 heure
SESSION_COOKIE_AGE = 3600

# Expire à la fermeture du navigateur (optionnel mais recommandé)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Ne prolonge pas la session automatiquement à chaque requête
SESSION_SAVE_EVERY_REQUEST = False

