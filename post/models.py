'''
models.py - это файл, который содержит все модели Django.

ORM - Object-Relational Mapping - это концепция, 
которая позволяет работать с базами данных, используя объекты и методы.
'''
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        db_table = 'tag'
        ordering = ['title']


class PostManager(models.Manager):
    def create_post(self, title, text, image):
        post = self.create(title=title.upper(), text=text, image=image)
        return post


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts', # default: user_set
        null=True,
    )
    image = models.ImageField(upload_to='meme_photos/', null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(
        Tag, 
        related_name='posts', # default: post_set
        blank=True
    )

    objects = PostManager()

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'post'
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments', # default: comment_set
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text}"
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comment'
        ordering = ['-created_at']



# class PostDetails(models.Model):
#     post = models.OneToOneField(
#         Post,
#         on_delete=models.CASCADE,
#     )
#     description = models.TextField()
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.post.title} - {self.views} - {self.likes} - {self.dislikes}"
    
#     class Meta:
#         verbose_name = 'Детали поста'
#         verbose_name_plural = 'Детали постов'
#         db_table = 'post_details'
#         ordering = ['-views']