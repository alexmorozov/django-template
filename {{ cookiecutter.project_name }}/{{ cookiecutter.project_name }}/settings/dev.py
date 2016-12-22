from {{ cookiecutter.project_name }}.settings.common import *  # NOQA

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

if not TEST:
    INSTALLED_APPS += ('debug_toolbar', )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )


INTERNAL_IPS = ['192.168.1.%d' % num for num in range(1, 255)]


def custom_show_toolbar(request):
    return DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': 'settings.dev.custom_show_toolbar',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(module)s: %(message)s'
        },
    },
    'require_debug_true': {
        '()': 'django.utils.log.RequireDebugTrue',
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        '{{ cookiecutter.project_name }}': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

if TEST:
    # Радикально ускоряет фабрики пользователей.
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

    INSTALLED_APPS += (
        'django_nose',
    )
