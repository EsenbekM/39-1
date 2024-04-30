'''
admin.py - это файл, который содержит настройки администратора Django.
'''

from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from post.models import Post, Comment, Tag


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    # readonly_fields = ('author', 'text', 'created_at', 'updated_at')
    # fields = ('author', 'text', 'created_at', 'updated_at')



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'author', 'tags')
        }),
        ('Date information', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'text')
    ordering = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CommentInline]
    # filter_horizontal = ('tags',)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)
        return queryset
    
    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     if request.user.is_superuser:
    #         return True
    #     return False
    
    # def has_change_permission(self, request: HttpRequest, obj: Any = None) -> bool:
    #     return False
    
    # def has_delete_permission(self, request: HttpRequest, obj: Any = None) -> bool:
        # return False
    


admin.site.register(Comment)
admin.site.register(Tag)
