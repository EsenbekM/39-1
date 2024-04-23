"""
urls.py - Это файл URL-адресов Django, который содержит все URL-адреса проекта.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from post.views import hello_view, main_view, post_list_view, post_detail_view, post_create_view, post_update_view


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", main_view, name='main_view'),
    path("hello/", hello_view, name='hello_view'),
    path("posts/", post_list_view, name='post_list_view'),
    path("posts/create/", post_create_view, name='post_create_view'),
    path("posts/<int:post_id>/", post_detail_view, name='post_detail_view'),
    path("posts/<int:post_id>/update/", post_update_view, name='post_update_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
