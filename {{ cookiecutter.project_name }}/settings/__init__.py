#--coding: utf8--

import os

from {{ cookiecutter.project_name }}.settings.common import *  # NOQA

DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

try:
    from local import *  # NOQA
except ImportError:
    pass
