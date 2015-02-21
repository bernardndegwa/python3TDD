"""
WSGI config for superlists project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
>>>>>>> merging
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
