import os

from .base import *  # noqa

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
ALLOWED_HOSTS = ["web1-django.herokuapp.com"]

SECURE_SSL_REDIRECT = True

STATICFILES_DIRS += [
    os.path.join(BASE_DIR, "webproject/build/static"),
    os.path.join(BASE_DIR, "build/"),
]
