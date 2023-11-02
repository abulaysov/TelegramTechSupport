from urllib.parse import parse_qs

from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token

from channels.db import database_sync_to_async


@database_sync_to_async
def get_user(token):
    try:
        return Token.objects.get(key=token).user
    except Token.DoesNotExist:
        return AnonymousUser()


class WSAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        query_args = parse_qs(scope["query_string"])
        token = query_args.get(b"token")
        if not token:
            scope["user"] = AnonymousUser()
            return await self.app(scope, receive, send)

        token = token[0].decode()
        scope["user"] = await get_user(token)

        return await self.app(scope, receive, send)
