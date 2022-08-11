from .base import *
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DEBUG = False
DEBUG = True

#ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['277e-179-62-84-59.sa.ngrok.io'] esto se cambia segun la url que te de ngrok, siempre tiene que estar en funcionamiento la aplicacion
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')
#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'sistema',
    #    'USER': 'matias',
     #   'PASSWORD': 'quiroga95',
      #  'HOST': 'localhost',
       # 'PORT': 5432
 #   }
EMAIL_BACKEND ="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "sistema.academico.ipes@gmail.com"
EMAIL_HOST_PASSWORD = "twrrnwyrawgxypma"
#EMAIL_HOST_PASSWORD = "ipes2021"