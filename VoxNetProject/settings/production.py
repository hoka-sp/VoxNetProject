from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','34.97.67.51','vox-net.com','www.vox-net.com']
CSRF_TRUSTED_ORIGINS = ['https://vox-net.com', 'https://www.vox-net.com']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/usr/share/nginx/html/media'
