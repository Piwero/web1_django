import os

from .base import *  # noqa

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
ALLOWED_HOSTS = ["piwero-django1.herokuapp.com"]

SECURE_SSL_REDIRECT = True

STATICFILES_DIRS += [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "build/static"),
    os.path.join(BASE_DIR, "build/"),
]
