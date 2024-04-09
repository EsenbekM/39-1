"""
WSGI - Web Server Gateway Interface. 
Это стандартный протокол, который используется для связи между 
веб-сервером и веб-приложением. WSGI позволяет веб-серверу передавать 
запросы веб-приложению и получать от него ответы. 
WSGI также позволяет веб-приложению работать с 
различными веб-серверами, не завися от их реализации.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meme.settings")

application = get_wsgi_application()
