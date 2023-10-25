from django.urls import path

from .views import ChatView

urlpatterns = [
    path('chats/', ChatView.as_view(), name='chats'),
]