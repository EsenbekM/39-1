"""
urls.py - Это файл URL-адресов Django, который содержит все URL-адреса проекта.
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from post.views import hello_view, main_view, post_list_view, post_detail_view, \
    post_create_view, post_update_view, HelloView, PostListView, PostDetailView, \
    PostCreateView, PostUpdateView

from user.views import LoginView, RegisterView, LogoutView, ProfileView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    
    path("", main_view, name='main_view'),

    path("hello/", hello_view, name='hello_view'),
    path("hello2/", HelloView.as_view(), name='hello_view2'),

    path("posts/", post_list_view, name='post_list_view'),
    path("posts2/", PostListView.as_view(), name='post_list_view2'),

    path("posts/create/", post_create_view, name='post_create_view'),
    path("posts2/create/", PostCreateView.as_view(), name='post_create_view2'),

    path("posts/<int:post_id>/", post_detail_view, name='post_detail_view'),
    path("posts2/<int:post_id>/", PostDetailView.as_view(), name='post_detail_view2'),

    path("posts/<int:post_id>/edit/", post_update_view, name='post_update_view'),
    path("posts2/<int:post_id>/edit/", PostUpdateView.as_view(), name='post_update_view2'),

    path("register/", RegisterView.as_view(), name='register_view'),
    path("login/", LoginView.as_view(), name='login_view'),
    path("logout/", LogoutView.as_view(), name='logout_view'),
    path("profile/", ProfileView.as_view(), name='profile_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
