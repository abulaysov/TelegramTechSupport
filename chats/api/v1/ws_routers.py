from django.urls import path

from . import consumers

ws_urlpatterns = [
    path(r"ws/", consumers.ChatAPIConsumer.as_asgi()),
]
