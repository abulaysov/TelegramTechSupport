from rest_framework import serializers

from users import models


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TelegramUser
        fields = ("id",)
