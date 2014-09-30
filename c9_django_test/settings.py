"""
Django settings for c9_django_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
USER_APPS = (
    'polls',
)

BUILT_IN_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS = USER_APPS + BUILT_IN_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'c9_django_test.urls'

WSGI_APPLICATION = 'c9_django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Detroit'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIR= (
    os.path.join(BASE_DIR, 'static',),
    # os.path.join(os.path.dirname(__file__), 'static',),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# common location for all static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # os.path.join(os.path.dirname(__file__), 'static',)


# Templates home
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
# TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]
# TEMPLATE_DIRS = (
#     # os.path.join(BASE_DIR, 'templates'),
#     os.path.join(os.path.dirname(__file__), 'templates'),
# )

# TEMPLATE_DIRS = ()

print ('BASE_DIR:\t{}'.format(BASE_DIR))
print (STATIC_ROOT)
print ('static files:\t{}'.format(STATICFILES_DIR))
print ('template files:\t{}'.format(TEMPLATE_DIRS))

try:
    from local_settings import *
except:
    pass
