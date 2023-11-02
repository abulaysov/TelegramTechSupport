import json

from django.core.cache import cache
from rest_framework import permissions

from djangochannelsrestframework.generics import AsyncAPIConsumer


class ChatAPIConsumer(AsyncAPIConsumer):
    permission_classes = [permissions.IsAuthenticated]

    async def connect(self):
        user = self.scope["user"]
        cache.set(f"ws-{user.pk}", self.channel_name, 86000)
        await super().connect()

    async def send_message(self, event):
        print(event)
        await self.send(text_data=json.dumps(event["data"]))

    async def disconnect(self, code):
        cache.delete(f"ws-{self.scope['user']}")
        await super().disconnect(code)
