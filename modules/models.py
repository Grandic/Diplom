from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Module(models.Model):
    """Модель модуля"""

    number = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=250, verbose_name='Описание')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                              **NULLABLE)

    def __str__(self):
        return f'Модуль{self.name}'

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'