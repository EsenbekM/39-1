"""
urls.py - Это файл URL-адресов Django, который содержит все URL-адреса проекта.
"""
from django.contrib import admin
from django.urls import path

from post.views import hello_view, main_view


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", main_view),
    path("hello/", hello_view)
]
