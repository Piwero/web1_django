from .base import *  # noqa

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
ALLOWED_HOSTS = ["piwero-django1.herokuapp.com"]

SECURE_SSL_REDIRECT = True
