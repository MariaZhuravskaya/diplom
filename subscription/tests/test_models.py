from django.test import TestCase
from content.models import Publication
from subscription.models import Subscription


class SubscriptionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        publication = Publication.objects.create(name='Big', description='Bob', price=12000, is_publication=True)
        Subscription.objects.create(publication=publication)

    def test_publication_label(self):
        subscription = Subscription.objects.get(id=1)
        field_label = subscription._meta.get_field('publication').verbose_name
        self.assertEquals(field_label, 'публикация')

    def test_user_label(self):
        subscription = Subscription.objects.get(id=1)
        field_label = subscription._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'пользователь подписки')

    def test_payments_label(self):
        subscription = Subscription.objects.get(id=1)
        field_label = subscription._meta.get_field('payments').verbose_name
        self.assertEquals(field_label, 'платеж')

    def test_paid_label(self):
        subscription = Subscription.objects.get(id=1)
        field_label = subscription._meta.get_field('is_active').verbose_name
        self.assertEquals(field_label, 'активность подписки')
