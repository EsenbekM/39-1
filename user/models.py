from django.db import models
from django.contrib.auth.models import User

from post.models import Post

# 1 вариант расщирения модели пользователя
# class Users(AbstractBaseUser):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     password = models.CharField(max_length=128)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     logo = models.ImageField(upload_to='logos/', null=True, blank=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

#     def __str__(self):
#         return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
