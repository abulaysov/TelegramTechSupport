"""
ASGI config for configs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import django
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings")


def get_ws_application():
    from users.ws_auth import WSAuthMiddleware  # noqa

    from .ws_urls import urlpatterns  # noqa

    django.setup(set_prefix=False)
    return WSAuthMiddleware(URLRouter(urlpatterns))


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": get_ws_application(),
    }
)
