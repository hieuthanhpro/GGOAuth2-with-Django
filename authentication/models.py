from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)  # Thêm unique=True
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'  # Trường dùng để đăng nhập
    REQUIRED_FIELDS = ['username']  # Các trường bắt buộc khi tạo superuser