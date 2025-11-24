from .base import *

DEBUG = True
SECRET_KEY = env('SECRET_KEY', default='django-insecure-local-key-for-dev')
ALLOWED_HOSTS = ['*']

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
