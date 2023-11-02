from configs import BaseService

from .data_classes import TelegramMessage


class TelegramMessageParser(BaseService):
    def __init__(self, data: dict):
        self._data = data

    def _parse(self) -> TelegramMessage:
        message = self._data["message"]
        return TelegramMessage(
            text=message["text"],
            chat_id=message["from"]["id"],
            message_id=message["message_id"],
        )

    def execute(self) -> TelegramMessage:
        return self._parse()
