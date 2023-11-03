"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from chats.api.v1.routers import urls as chats_v1_routers
from users.api.v1.routers import urls as users_v1_routers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api_docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path("", include("chats.urls")),
    path("", include("users.urls")),
    *users_v1_routers,
    *chats_v1_routers,
    re_path(
        r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}
    ),
    re_path(
        r'^static/(?P<path>.*)$',
        serve,
        {'document_root': settings.STATIC_ROOT},
    ),
]

