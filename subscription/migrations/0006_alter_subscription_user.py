# Generated by Django 4.2.8 on 2023-12-21 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0005_alter_subscription_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь подписки'),
        ),
    ]
