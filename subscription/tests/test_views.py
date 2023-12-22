from django.test import TestCase
from django.urls import reverse

from content.models import Publication
from subscription.models import Subscription


class SubscriptionListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        publication = Publication.objects.create(name='Big', description='Bob', price=12000, is_publication=True)
        Subscription.objects.create(publication=publication)
        Subscription.objects.create(publication=publication)
        Subscription.objects.create(publication=publication)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('subscription:subscription_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('subscription:subscription_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'subscription/subscription_list.html')
