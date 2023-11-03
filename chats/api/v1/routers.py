from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register("v1/chats/messages", views.MessageViewSet, "messages")
router.register("v1/chats/bots", views.BotViewSet, "bots")

urls = router.urls
