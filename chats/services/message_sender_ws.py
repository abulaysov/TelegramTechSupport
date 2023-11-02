from django.contrib.auth import get_user_model
from django.core.cache import cache

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from chats import models
from configs import BaseService


class MessageSenderWS(BaseService):
    def __init__(self, message: models.Message):
        self._message = message

    def _get_data(self) -> dict:
        return dict(
            id=self._message.chat.telegram_user.id, text=self._message.text
        )

    def _send(self) -> None:
        users = get_user_model().objects.all()
        data = self._get_data()
        for user in users:
            channel_name = cache.get(f"ws-{user.pk}")
            if not channel_name:
                continue
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.send)(
                channel_name,
                {"type": "send.message", "data": data},
            )

    def execute(self) -> None:
        self._send()
