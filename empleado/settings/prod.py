
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'kevapp',
        'PASSWORD': 'kevin',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child('media')
