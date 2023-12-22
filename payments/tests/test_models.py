from django.test import TestCase

from content.models import Publication
from payments.models import Payments
from users.models import User


class PaymentsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test', password='12345')
        user.save()
        publication = Publication.objects.create(name='Big', description='Bob', price=12000, is_publication=True)
        Payments.objects.create(user=user.pk, publication=publication.pk)

    def test_user_label(self):
        payments = Payments.objects.get(id=1)
        field_label = payments._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'пользователь')

    def test_publication_label(self):
        payments = Payments.objects.get(id=1)
        field_label = payments._meta.get_field('publication').verbose_name
        self.assertEquals(field_label, 'публикация')
