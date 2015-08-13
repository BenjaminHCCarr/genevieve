"""
Django settings for genevieve_client project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

from django.conf import global_settings
from env_tools import apply_env

from .utils import to_bool

# Apply the environment variables in the .env file.
apply_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = to_bool('DEBUG', 'true')
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Required by django-allauth
    'django.contrib.sites',

    # Main app for the site.
    'genevieve_client',

    # Third party apps
    'allauth',
    'allauth.account',
    'debug_toolbar',
    'template_timings_panel',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # Required by 'allauth' template tags
    'django.core.context_processors.request',

    # 'allauth' specific context processors
    'allauth.account.context_processors.account',
) + global_settings.TEMPLATE_CONTEXT_PROCESSORS


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',

    # 'allauth' specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
) + global_settings.AUTHENTICATION_BACKENDS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'genevieve_client.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'genevieve_client.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Email set up.
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', global_settings.EMAIL_BACKEND)
EMAIL_USE_TLS = to_bool('EMAIL_USE_TLS', str(global_settings.EMAIL_USE_TLS))
EMAIL_HOST = os.getenv('EMAIL_HOST', global_settings.EMAIL_HOST)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', global_settings.EMAIL_HOST_USER)
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD',
                                global_settings.EMAIL_HOST_PASSWORD)
EMAIL_PORT = int(os.getenv('EMAIL_PORT', str(global_settings.EMAIL_PORT)))

# Where to locally store files
LOCAL_STORAGE_ROOT = os.path.join(BASE_DIR, 'files/')
# Where to store uploaded files
MEDIA_ROOT = os.path.join(LOCAL_STORAGE_ROOT, 'upload/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Settings for django-allauth and account interactions.
# Signup and login take both email and username.
# No email confirmation is implemented.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# Site admin settings
SUPPORT_EMAIL = os.getenv('SUPPORT_EMAIL')

LOGIN_REDIRECT_URL = 'home'

# Django debug toolbar settings
# http://django-debug-toolbar.readthedocs.org/en/latest/configuration.html#debug-toolbar-panels
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.sql.SQLPanel',
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
]

# GenNotes client ID and secret.
GENNOTES_CLIENT_ID = os.getenv('GENNOTES_CLIENT_ID')
GENNOTES_CLIENT_SECRET = os.getenv('GENNOTES_CLIENT_SECRET')
GENNOTES_REDIRECT_URI = os.getenv('GENNOTES_REDIRECT_URI',
                                  'http://localhost:8000/authorize_gennotes/')
