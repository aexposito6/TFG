"""
WSGI config for arbitros project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

#sys.path.append("/home/antonio/TFG/arbitros/arbitros")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arbitros.settings")

application = get_wsgi_application()
