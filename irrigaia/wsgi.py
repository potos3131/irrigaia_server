"""
WSGI config for irrigaia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'irrigaia.settings')
ENV_DTI = True
if (ENV_DTI):
    os.environ['http_proxy'] = "http://proxy:8080"
    os.environ['https_proxy'] = "http://proxy:8080"
application = get_wsgi_application()
