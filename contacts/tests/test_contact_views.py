from django.test import TestCase
from django.urls import reverse

from contacts.models import Contact


class ContactListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_contact = 3
        for contact_num in range(number_of_contact):
            Contact.objects.create(name='Maria %s' % contact_num, phone='+79205552211 %s' % contact_num,
                                   message='Hello, world! %s' % contact_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('contacts:contact_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('contacts:contact_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'contacts/contact_list.html')
