from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='zhuravsckajam@yandex.ru',
            phone='+79205862225',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('maria')
        user.save()
