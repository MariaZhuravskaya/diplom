from django.db import models

from config import settings
from content.models import Publication
from payments.models import Payments


class Subscription(models.Model):
    """
    Модель подписки
    """
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='публикация')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='пользователь подписки')
    is_active = models.BooleanField(default=False, verbose_name='активность подписки')
    payments = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, verbose_name='платеж')

    def __str__(self):
        return f'{self.user}{self.publication}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
