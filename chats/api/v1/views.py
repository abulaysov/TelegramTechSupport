from rest_framework import status, viewsets
from rest_framework.response import Response

from chats import models, services
from users.services import TelegramUserCreator

from . import serializers


class BotViewSet(viewsets.ViewSet):
    schema = None

    def create(self, request):  # noqa
        message = services.TelegramMessageParser(data=request.data).execute()
        if message.text == "/start":
            TelegramUserCreator(telegram_id=message.chat_id).execute()
        else:
            services.MessageCreator(tg_message=message).execute()
        return Response(status=status.HTTP_200_OK)


class MessageViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.MessageCreateSerializer
    queryset = models.Message.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        chat = data.get("chat")
        text = data.get("text")
        services.TelegramMessageSender(
            text=text, tg_chat_id=chat.telegram_user.id
        ).execute()
        return Response(status=status.HTTP_201_CREATED)
