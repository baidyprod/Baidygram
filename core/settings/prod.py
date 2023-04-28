import os
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['EXTERNAL IP OF CLOUD GOOGLE COM INSTANCE']
