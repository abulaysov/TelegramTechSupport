import requests

from chats import services
from configs import BaseService
from configs.settings import TELEGRAM_API_TEMPLATE

from .data_classes import TelegramMessage


class TelegramMessageSender(BaseService):
    def __init__(self, text: str, tg_chat_id: int):
        self._text = text
        self._tg_chat_id = tg_chat_id
        self._method = "sendMessage"

    def _send(self) -> dict:
        response = requests.get(
            TELEGRAM_API_TEMPLATE.format(method=self._method),
            params={
                "chat_id": self._tg_chat_id,
                "text": self._text,
            },
        ).json()
        return response

    def _parse_message(self, tg_message: dict) -> TelegramMessage:
        message = tg_message["result"]
        message_id = message["message_id"]
        text = message["text"]
        chat_id = message["chat"]["id"]
        is_bot = True

        return TelegramMessage(
            message_id=message_id,
            text=text,
            chat_id=chat_id,
            is_bot=is_bot,
        )

    def execute(self) -> None:
        tg_message: dict = self._send()
        tg_message: TelegramMessage = self._parse_message(tg_message)
        services.MessageCreator(tg_message=tg_message).execute()
