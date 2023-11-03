import re
from typing import NoReturn

from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from chats import models
from users.services import TokenGetter


class ChatView(LoginRequiredMixin, View):
    login_url = "login"
    # re

    def get(self, request):
        is_chat = self._get_chat_param()
        if not is_chat:
            user_token = TokenGetter(username=request.user.username).execute()
            request.session["auth_token"] = user_token
            return render(request, "chats/index.html")

        chat = self._get_chat()
        context_data = {"current_chat": chat}
        return render(request, "chats/index.html", context=context_data)

    def _get_chat_param(self) -> str | None:
        return self.request.GET.get("chat")  # noqa

    def _get_chat(self) -> models.Chat | NoReturn:
        chat_id = self._get_chat_param()
        if not self._validate_chat_param(chat_id):
            raise Http404()

        chat = (
            models.Chat.objects.select_related("telegram_user")
            .prefetch_related("messages")
            .filter(pk=chat_id)
            .first()
        )
        if not chat:
            raise Http404()

        return chat

    def _validate_chat_param(self, param: str):
        if re.fullmatch(r"\d+", self._get_chat_param()):
            return True
        return False

