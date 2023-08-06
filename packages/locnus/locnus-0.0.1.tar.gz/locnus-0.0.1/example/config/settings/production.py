"""
Django settings for locnus project in production mode

This fill will be automatically used when using a dedicated application server.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""


from .base import *  # noqa
from .base import env

environ.Env.read_env(BASE_DIR / ".env")  # noqa

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# remember to set this to your expected hostnames
ALLOWED_HOST = env("ALLOWED_HOST")
ALLOWED_HOSTS = [ALLOWED_HOST]

# static files
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Custom Admin URL, use  {% url 'admin:index' %}
ADMIN_URL = env("DJANGO_ADMIN_URL")
