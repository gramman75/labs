# -*- encoding:utf8 -*-
"""
Django settings for labs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!us=q^g&iue%ryq89)@r4mkqa@7&f4pkzalq=38xze0cy)wp^*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SOCKETIO_HOST = '1.1.1.1'
SOCKETIO_PORT = '80'
# template context processor
TEMPLATE_CONTEXT_PROCESSORS = (    
    'django.core.context_processors.csrf',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    )

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tweeter',
    'labs',
    'djangular',
    'todo',
    'board',
    'django_socketio',
    'chat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'labs.urls'

WSGI_APPLICATION = 'labs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = (
#os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'static/templates'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file_handler' : {
            'level' : 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter' : 'verbose',
            'filename' : os.path.join(BASE_DIR,'log/logconfig.txt')
            }               
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'file' : {
             'handlers' : ['file_handler'],
             'level' : 'DEBUG'
             }
    }
}

#로그인 정보가 없을 경우 이동하는 페이지
LOGIN_URL = 'http://127.0.0.1:8000/#/login/'

#user profile
AUTH_PROFILE_MODULE = 'labs.UserProfile'

#session store method
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

#whether to expire the session when close browser.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# REST_FRAMEWORK = {
#     'PAGINATE_BY': 10,                 # Default to 10
#     'PAGINATE_BY_PARAM': 5,  # Allow client to override, using `?page_size=xxx`.
#     'MAX_PAGINATE_BY': 100             # Maximum limit allowed when using `?page_size=xxx`.
# }
