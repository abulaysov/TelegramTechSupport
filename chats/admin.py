from django.contrib import admin

from chats import models


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ["id", "telegram_user"]


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
