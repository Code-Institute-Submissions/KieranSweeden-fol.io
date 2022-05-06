"""
Django settings for folio project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e0+8kwv(u8jk5fv=ok0@p=+l=xk5!87-q2-(v%l-rr)7^xxo(&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'folio-web-app.herokuapp.com',
    'localhost'
]

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # required by allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #CORS
    'corsheaders',

    # required by crispy forms
    'crispy_forms',
    'crispy_bootstrap5',

    # fol.io specific apps
    'home',
    'library',
    'suite',
    'license',
    'account.__init__.AccountConfig',
    'showcase'
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'folio.urls'

CORS_ORIGIN_ALLOW_ALL = True 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # adding the route template directories
            os.path.join(BASE_DIR, "templates"),

            # adding our custom allauth directory to template dirs setting
            os.path.join(BASE_DIR, "templates", "allauth")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # required by allauth
                'django.template.context_processors.request'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

SITE_ID = 1

WSGI_APPLICATION = 'folio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.MinimumLengthValidator'),
    },
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.NumericPasswordValidator'),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# tells allauth that we want to allow authentication
# using only emails
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# make emails required with verification &
# make user enter email twice to reduce likelihood of typos
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# a minimum username length
ACCOUNT_USERNAME_MIN_LENGTH = 4

# url when logging in
LOGIN_URL = '/accounts/login/'

# url to be redirected to when logged in
LOGIN_REDIRECT_URL = '/library/'

WSGI_APPLICATION = 'folio.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# CSRF
if "DEVELOPMENT" in os.environ:

    url_partitions = os.environ.get('GITPOD_WORKSPACE_URL').partition('kieran')

    csrf_string = (
        f"{url_partitions[0]}*8000-"
        f"{url_partitions[1]}{url_partitions[2]}"
    )

    CSRF_TRUSTED_ORIGINS = [(csrf_string)]


# URL
if "DEVELOPMENT" in os.environ:
    URL_SECTIONS = os.environ.get('GITPOD_WORKSPACE_URL').partition('kieran')

    URL = (
        f'{URL_SECTIONS[0]}8000-{URL_SECTIONS[1]}{URL_SECTIONS[2]}/'
    )

else:
    URL = os.environ.get('URL')

# Stripe keys
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
STRIPE_PRIVATE_KEY = os.environ.get("STRIPE_PRIVATE_KEY")
STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET')
FOLIO_LICENSE_PRICE_ID = os.environ.get("FOLIO_LICENSE_PRICE_ID")

# S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_ACCESS_KEY_ID = os.environ.get('S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'folio-project'
AWS_QUERYSTRING_AUTH = False

# Email
if 'DEVELOPMENT' in os.environ:
    # Default email
    DEFAULT_FROM_EMAIL = "folio@gmail.com"
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

if "USE_AWS" in os.environ:

    # Static & media files
    # For static file storage we want to use our
    # StaticStorage class
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

    # The location django should save to is a folder
    # named static
    STATICFILES_LOCATION = 'static'
