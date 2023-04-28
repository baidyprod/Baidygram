import os
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['EXTERNAL SEVER IP', 'DOMAIN NAME', 'ANOTHER DOMAIN NAME ETC']
