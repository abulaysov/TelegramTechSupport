from chats import models
from configs import BaseService

# from chats import services
from .data_classes import TelegramMessage
from .message_sender_ws import MessageSenderWS


class MessageCreator(BaseService):
    def __init__(self, tg_message: TelegramMessage):
        self._tg_message = tg_message

    def execute(self) -> models.Message:
        message = self._create()
        if not message.is_bot:
            self._send_message_ws(message)
        return message

    def _create(self) -> models.Message:
        chat = self._get_chat()
        message = models.Message(
            message_id=self._tg_message.message_id,
            text=self._tg_message.text,
            chat=chat,
        )
        if self._tg_message.is_bot:
            message.is_bot = True
        message.save()
        return message

    def _get_chat(self) -> models.Chat:
        chat = models.Chat.objects.get(
            telegram_user__id=self._tg_message.chat_id
        )
        return chat

    @staticmethod
    def _send_message_ws(message) -> None:
        MessageSenderWS(message=message).execute()
