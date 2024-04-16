'''
admin.py - это файл, который содержит настройки администратора Django.
'''

from django.contrib import admin

from post.models import Post, Comment, Tag


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
