import factory.fuzzy
from factory.django import DjangoModelFactory

from users import models


class BaseUserFactory(DjangoModelFactory):
    class Meta:
        model = models.User


class ActiveUserFactory(BaseUserFactory):
    username = factory.Sequence(lambda n: 'username_{}'.format(n))


class BaseUserFactory(DjangoModelFactory):
    class Meta:
        model = models.TelegramUser

    id = factory.Sequence(lambda n: n)
