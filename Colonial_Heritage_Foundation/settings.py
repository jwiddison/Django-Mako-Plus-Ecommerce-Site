"""
Django settings for Colonial_Heritage_Foundation project.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ev7u&fkgfpw@im3ez*40sx3qpof_r^=7p5&**$_+nf+6*u=cs^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Stuff for Sprint 5.
STRIPE_SECRET_KEY = 'sk_test_kw7mgQceM2YnfMC4Zrsur8sb'
STRIPE_PUBLIC_KEY = 'pk_test_MHyCTSEPuZxOaIsMh4RIFcbB'
GOOGLE_SERVER_KEY = 'AIzaSyBPic4S2IEKGVinGhN61E5Fy42s8nu3DEA'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Easy way?
# EMAIL_HOST = 'gateway.byu.edu'

# Chfsales.com way?
# EMAIL_HOST = 'mail.chfsales.com'
# EMAIL_HOST_USER = 'orders@chfsales.com'
# EMAIL_HOST_PASSWORD = 'Group12ia!'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 25

# Gmail way?
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chfnoreply@gmail.com'
EMAIL_HOST_PASSWORD = 'w0lfp@ck'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'Colonial Heritage Foundation <chfnoreply@gmail.com>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus.controller',
    'account',
    'api',
    'catalog',
    'homepage',
    'manager',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Colonial_Heritage_Foundation.shopping_cart.ShoppingCartMiddleware',
    'django_mako_plus.controller.router.RequestInitMiddleware',
]

ROOT_URLCONF = 'Colonial_Heritage_Foundation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Colonial_Heritage_Foundation.wsgi.application'

# Override Django user models
AUTH_USER_MODEL = 'account.User'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Colonial_Heritage_Foundation',
        'USER': 'postgres',
        'PASSWORD': 'DbAdminLocal',
        'HOST': 'localhost',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
 # SECURITY WARNING: this next line must be commented out at deployment
 BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # never set this True on a live site
LOGGING = {
 'version': 1,
 'disable_existing_loggers': True,
 'formatters': {
     'simple': {
         'format': '%(levelname)s %(message)s'
     },
 },
 'handlers': {
     'console':{
         'level':'DEBUG',
         'class':'logging.StreamHandler',
         'formatter': 'simple'
     },
 },
 'loggers': {
     'django_mako_plus': {
         'handlers': ['console'],
         'level': 'DEBUG',
         'propagate': False,
     },
 },
}

###############################################################
###   Specific settings for the Django-Mako-Plus app
DJANGO_MAKO_PLUS = {
 # identifies where the Mako template cache will be stored, relative to each app
 'TEMPLATES_CACHE_DIR': 'cached_templates',

 # the default app and page to render in Mako when the url is too short
 'DEFAULT_PAGE': 'index',
 'DEFAULT_APP': 'homepage',

 # the default encoding of template files
 'DEFAULT_TEMPLATE_ENCODING': 'utf-8',

 # these are included in every template by default - if you put your most-used libraries here, you won't have to import them exlicitly in templates
 'DEFAULT_TEMPLATE_IMPORTS': [
   'import os, os.path, re, json',
 ],

 # see the DMP online tutorial for information about this setting
 'URL_START_INDEX': 0,

 # whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
 # determines whether DMP will send its custom signals during the process
 'SIGNALS': True,

 # whether to minify using rjsmin, rcssmin during 1) collection of static files, and 2) on the fly as .jsm and .cssm files are rendered
 # rjsmin and rcssmin are fast enough that doing it on the fly can be done without slowing requests down
 'MINIFY_JS_CSS': True,

 # see the DMP online tutorial for information about this setting
 'TEMPLATES_DIRS': [
   # '/var/somewhere/templates/',
 ],
}
###  End of settings for the Django-Mako-Plus
################################################################
