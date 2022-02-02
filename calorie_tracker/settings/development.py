# This file will contain settings you’ll normally use during development.
from .base import *

DEBUG = True

ALLOWED_HOSTS = [s.strip().replace('\'', '') for s in os.environ.get('DEVELOPMENT_ALLOWED_HOSTS').split(',')]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER'),
        'PASSWORD': os.environ.get('SQL_PASSWORD'),
        'HOST': os.environ.get('SQL_HOST'),
        'PORT': os.environ.get('SQL_PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, '/static')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'staticfiles')
# ]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
