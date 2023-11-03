from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from users import models


class LoginView(View):

    def get(self, request):  # noqa
        return render(request, "users/login.html")

    def post(self, request):
        password = request.POST.get("password")
        user = models.User.objects.first()
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("chats")
        return render(request, "users/login.html")

