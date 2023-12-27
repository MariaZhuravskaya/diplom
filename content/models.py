from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Publication(models.Model):
    """
    Модель публикации
    """
    name = models.CharField(max_length=250, verbose_name='наименование статьи')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='content/', **NULLABLE, verbose_name='изображение')
    paid = models.BooleanField(default=False, verbose_name='бесплатная/платная публикация')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='стоимость подписки')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_change = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    number_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    is_publication = models.BooleanField(default=True, verbose_name='опубликовано')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                               verbose_name='автор статьи')

    def __str__(self):
        return f"{self.name}, {self.price}"

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
