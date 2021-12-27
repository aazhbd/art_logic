from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-+c$%+(&oaw(0x53ah@#1$s)-xh7r#d#d#$5q*k*ujn%7gt*_y2'

ALLOWED_HOSTS = ['articulatedlogic.com', 'www.articulatedlogic.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
