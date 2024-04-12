'''
models.py - это файл, который содержит все модели Django.

ORM - Object-Relational Mapping - это концепция, 
которая позволяет работать с базами данных, используя объекты и методы.
'''
from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='meme_photos/', null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'post'
        ordering = ['-created_at']
