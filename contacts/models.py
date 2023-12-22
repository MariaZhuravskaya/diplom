from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=16, verbose_name='Телефон', **NULLABLE)
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.message}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
