from .base import *
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DEBUG = False
DEBUG = True

#ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['277e-179-62-84-59.sa.ngrok.io'] esto se cambia segun la url que te de ngrok, siempre tiene que estar en funcionamiento la aplicacion
ALLOWED_HOSTS = ['saipes.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2o0mltitd7794',
        'USER': 'xcpbyxxeyumykt',
        'PASSWORD': 'ddbbccf6cd430094c75694439cb79a602addd26e9085d0eeb2bae35ee4a0d500',
        'HOST': 'ec2-44-206-197-71.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')

EMAIL_BACKEND ="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "sistema.academico.ipes@gmail.com"
EMAIL_HOST_PASSWORD = "twrrnwyrawgxypma"
#EMAIL_HOST_PASSWORD = "ipes2021"