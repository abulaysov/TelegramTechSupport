from django.db import models


class Chat(models.Model):
    telegram_user = models.OneToOneField(
        "users.TelegramUser", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.telegram_user)
