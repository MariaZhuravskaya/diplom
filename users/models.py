from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    phone = models.CharField(unique=True, max_length=12, verbose_name='телефон')
    email = models.EmailField(unique=True, verbose_name='почта', **NULLABLE)
    password = models.CharField(unique=True, verbose_name='пароль')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    first_name = models.CharField(max_length=20, verbose_name='имя пользователя')
    last_name = models.CharField(max_length=20, verbose_name='фамилия пользователя')
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
