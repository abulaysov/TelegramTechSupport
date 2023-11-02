from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from configs import BaseService


class TokenGetter(BaseService):
    def __init__(self, username: str):
        self._username = username

    def execute(self) -> str | None:
        users = get_user_model().objects.filter(username=self._username)
        if not users.exists():
            return
        user = users.first()
        token, _ = Token.objects.get_or_create(user=user)
        return token.key
