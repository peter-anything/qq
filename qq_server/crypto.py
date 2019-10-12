import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'crypto_settings'
from django.contrib.auth.hashers import make_password, check_password

def generate_password(password):
    return make_password(password, None)

check_password = check_password