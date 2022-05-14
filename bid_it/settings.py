import django_heroku
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u&u)*)c5cl@^syz^*5kq0^em#+3fu7(!=n1mjpoh$i5heoc_t2'

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('DJANGO_ENVIRONMENT') == 'PRODUCTION':
    DEBUG = False
else:
    DEBUG = True


ALLOWED_HOSTS = ['https://bid-bud.herokuapp.com/login/',"localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bid_it.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'bid_it.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#database for local dbsqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#database for local database postgresql
# DATABASES={
#    'default':{
#       'ENGINE':'django.db.backends.postgresql_psycopg2',
#       'NAME':'nirmal1',
#       'USER':'postgres',
#       'PASSWORD':'bhovan123#',
#       'HOST':'localhost',
#       'PORT':'5432',
#    }
# }
##database for deploying in heroku
DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME':'d6idvuom7bk6tn',
      'USER':'jsuvsvsuplifar',
      'PASSWORD':'37bdd1ba5ce98e5ad7e5e49359cf4d698ddff887bea8a9199020f638b8da3caa',
      'HOST':'ec2-52-201-124-168.compute-1.amazonaws.com',
      'PORT':'5432',
   }
}
dj_from_env=dj_database_url.config(conn_max_age=200)
DATABASES['default']=dj_database_url.config(default='postgres://jsuvsvsuplifar:37bdd1ba5ce98e5ad7e5e49359cf4d698ddff887bea8a9199020f638b8da3caa@ec2-52-201-124-168.compute-1.amazonaws.com:5432/d6idvuom7bk6tn')
DATABASES['default'].update(dj_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


LOGIN_URL='/login/'



# Activate Django-Heroku.
django_heroku.settings(locals(),databases=True)