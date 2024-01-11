from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager

NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=50, verbose_name='Name', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
