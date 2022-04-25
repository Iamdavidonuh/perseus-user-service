from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=ayexi9227uy*r*(aj+jmnvy7i*#bl+-@yj9i7vr3^4v1q^u)9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
