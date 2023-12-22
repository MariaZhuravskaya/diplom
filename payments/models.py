from django.db import models
from content.models import Publication
from users.models import User


class Payments(models.Model):
    """
     Модель описывающая платеж
     """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='публикация')




