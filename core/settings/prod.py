import os
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['EXTERNAL SERVER IP', 'DOMAIN NAME', 'ANOTHER DOMAIN NAME ETC']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'password'
NOREPLY_EMAIL = 'noreply email'
CONTACT_EMAIL = 'contact email'
