'''
admin.py - это файл, который содержит настройки администратора Django.
'''

from django.contrib import admin

from post.models import Post


admin.site.register(Post)

