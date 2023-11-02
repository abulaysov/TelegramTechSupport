from rest_framework import serializers

from chats import models


class MessageCreateSerializer(serializers.Serializer):
    text = serializers.CharField()
    chat = serializers.PrimaryKeyRelatedField(
        queryset=models.Chat.objects.all()
    )
