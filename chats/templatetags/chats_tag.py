from django import template
from django.db.models import OuterRef, Subquery

from chats import models

register = template.Library()


@register.simple_tag
def get_all_chats():
    chats = (
        models.Chat.objects.select_related("telegram_user")
        .annotate(
            last_message=Subquery(
                models.Message.objects.filter(chat_id=OuterRef("pk"))
                .order_by("-created_at")
                .values("text")[:1]
            )
        )
        .all()
    )

    return chats
