"""
ASGI - Asynchronous Server Gateway Interface
ASGI is a spiritual successor to WSGI, 
intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meme.settings")

application = get_asgi_application()
