from chats.models import Chat
from configs import BaseService
from users import models


class TelegramUserCreator(BaseService):
    def __init__(self, telegram_id: int):
        self._telegram_id = telegram_id

    def execute(self) -> models.TelegramUser:
        tg_user = self._create()
        return tg_user

    def _create(self) -> models.TelegramUser:
        try:
            tg_user = models.TelegramUser.objects.get(id=self._telegram_id)
        except models.TelegramUser.DoesNotExist:
            tg_user = models.TelegramUser.objects.create(id=self._telegram_id)
            self._create_chat(tg_user=tg_user)
        return tg_user

    def _create_chat(self, tg_user: models.TelegramUser):  # noqa
        Chat.objects.create(telegram_user=tg_user)
