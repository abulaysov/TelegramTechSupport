from django.db import models


class TelegramUser(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    username = models.CharField(max_length=255, blank=True, null=True)
    is_moder = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id} | Username: {self.username}"
