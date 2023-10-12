"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pathlib import Path
import os

from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "testdfdsfsdkl"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ["*"]

BACK_PROTOCOL = os.getenv("BACK_PROTOCOL")
BACK_HOST = os.getenv("BACK_HOST")
BACK_PORT = os.getenv("BACK_PORT", 8213)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "back_app",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "back.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "back.wsgi.application"

DB_MOTEUR_ENGINE = os.getenv("DB_MOTEUR_ENGINE", "django.db.backends.mysql")
DB_MOTEUR_NAME = os.getenv("DB_MOTEUR_NAME", None)  # mysql database name
DB_MOTEUR_NAME_TEST = os.getenv("DB_MOTEUR_NAME_TEST", None)  # mysql database test name
DB_MOTEUR_USER = os.getenv("DB_MOTEUR_USER", None)
DB_MOTEUR_PASSWORD = os.getenv("DB_MOTEUR_PASSWORD", None)
DB_MOTEUR_HOST = os.getenv("DB_MOTEUR_HOST", "linkmysql")
DB_MOTEUR_PORT = os.getenv("DB_MOTEUR_PORT", "3306")
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATABASES = {
    "default": {
        "ENGINE": DB_MOTEUR_ENGINE,
        "NAME": DB_MOTEUR_NAME,
        "USER": DB_MOTEUR_USER,
        "PASSWORD": DB_MOTEUR_PASSWORD,
        "HOST": DB_MOTEUR_HOST,
        "PORT": DB_MOTEUR_PORT,
        "ATOMIC_REQUESTS": True,
        "TEST": {
            "NAME": DB_MOTEUR_NAME_TEST,
        },
    },
}


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,  # Clé secrète de votre application
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer","JWT"),
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "SLIDING_TOKEN_REFRESH": False,
    "SLIDING_TOKEN_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_REFRESH_GRACE_PERIOD": timedelta(days=0),
}

# Exemple de réglage de la durée de vie du token de rafraîchissement (facultatif)
SIMPLE_JWT["JWT_REFRESH_TOKEN_LIFETIME"] = timedelta(days=30)
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOG_DIR = os.path.join(BASE_DIR, "log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(name)s.%(funcName)s:%(lineno)s - %(message)s"
        },
        "simple": {"format": "%(asctime)s %(levelname)s %(module)s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOG_DIR, "debug.log"),
            "maxBytes": 100000000,  # around 100 MB
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "jam": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "resource": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": True,
        },
        "django": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}
