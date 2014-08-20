"""
Django settings for FineLineIOSApp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Braintree settings go here
import braintree
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                    merchant_id='qwy245r24sttxftk',
                                    public_key='wx9h8st6d2vyb7nz',
                                    private_key='4bbfb9b4be77ff456b287cf467d9fd1f')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c_z@c$*lsg)7=fq!kqmwf5tvy-i*g*t3y-&^+dr^@)ipn7kx8f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'FineLineIOSApp.partyorders',
    'FineLineIOSApp.payment',
    'FineLineIOSApp.company_website',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'FineLineIOSApp.urls'

WSGI_APPLICATION = 'FineLineIOSApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fineline',
        'USER': 'root',
        'PASSWORD': 'test123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

DATABASES['default'] =  dj_database_url.parse("mysql://b68bc60bf51344:6b30b057@us-cdbr-iron-east-01.cleardb.net/heroku_59892ff05168b27?reconnect=true")

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
            os.path.join(BASE_DIR, 'FineLineIOSApp/partyorders/files'),
            )
