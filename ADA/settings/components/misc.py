from decouple import config, Csv
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# GIT_HASH = fetch_git_sha(os.path.dirname(os.pardir))

AdminSite.site_title = ugettext_lazy('IMS Admin')
AdminSite.site_header = ugettext_lazy('IMS Administration')
AdminSite.index_title = ugettext_lazy('IMS ADMINISTRATION')

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
#DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROOT_URLCONF = 'ADA.urls'
WSGI_APPLICATION = 'ADA.wsgi.application'
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost, 127.0.0.1', cast=Csv())
INTERNAL_IPS = config('INTERNAL_IPS', default='127.0.0.1', cast=Csv())

# use ses for email
# EMAIL_BACKEND = 'django_ses.SESBackend'
#
# MINIMUM_APP_VERSION = float(config('MINIMUM_APP_VERSION', 0))
#
# DEFAULT_FROM_EMAIL = "Cookups <support@cookupsapp.com>"
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10mb
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10mb