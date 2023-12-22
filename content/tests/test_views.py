from django.test import TestCase
from django.urls import reverse

from content.models import Publication


class PublicationListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_publication = 13
        for publication_num in range(number_of_publication):
            Publication.objects.create(name='Big %s' % publication_num, description='Bob %s' % publication_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/publication')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('content:publication_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('content:publication_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'content/publication_list.html')
