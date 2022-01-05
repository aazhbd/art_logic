from .base import *

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEBUG = False

SECRET_KEY = '4rl!k3#gt@(7n(611^l@8(41+dgyupvqo-t3krb&#w@aw#u_er'

ALLOWED_HOSTS = ['articulatedlogic.com', 'www.articulatedlogic.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
