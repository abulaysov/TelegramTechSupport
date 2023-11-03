from django.db import models


class Message(models.Model):
    text = models.TextField()
    message_id = models.BigIntegerField()

    is_bot = models.BooleanField(default=False)
    was_read = models.BooleanField(default=False)

    chat = models.ForeignKey(
        "chats.Chat", on_delete=models.CASCADE, related_name="messages"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:10]} | Chat: {self.chat}"
