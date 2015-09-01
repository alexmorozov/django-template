# --coding: utf8--

import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def path(*a):
    return os.path.join(PROJECT_ROOT, *a)

# This trick allows to import apps without that prefixes
sys.path.insert(0, path('apps'))
sys.path.insert(0, path('libs'))
sys.path.insert(1, path('.'))

TEST = 'test' in sys.argv

ALLOWED_HOSTS = ['{{ cookiecutter.site_name }}']

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MEDIA_ROOT = path('../media')
STATIC_ROOT = path('../../static')

STATICFILES_DIRS = (
    path('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'
WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'djangobower',
    'hamlpy',
    'pipeline',
    'lib',
)


HAML_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'hamlpy.template.loaders.HamlPyFilesystemLoader',
        'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
    )),
)

COMMON_TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_LOADERS = HAML_LOADERS + COMMON_TEMPLATE_LOADERS
TEMPLATE_DIRS = (
    path('templates'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP  # NOQA

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

STATICFILES_FINDERS += (
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = path('static')
BOWER_INSTALLED_APPS = (
)

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None
PIPELINE_DISABLE_WRAPPER = True

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
)

# Параметры для удобного запуска ./manage.py shell_plus --notebook
IPYTHON_ARGUMENTS = [
    '--ext', 'django_extensions.management.notebook_extension',
    '--no-browser',
    '--ip', '0.0.0.0',
]
