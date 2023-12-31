# Generated by Django 4.2.8 on 2023-12-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_publication',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AddField(
            model_name='publication',
            name='number_views',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]
