from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from content.models import Publication


class PublicationListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_publication = 13
        for publication_num in range(number_of_publication):
            Publication.objects.create(name='Big %s' % publication_num, description='Bob %s' % publication_num, )

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


class PublicationViewTest(TestCase):

    def setUp(self) -> None:
        """
        Подготовка данных перед каждым тестом
        """
        self.publication = Publication.objects.create(name='Maria', description='Hello, world!')

    def test_retrieve_publication(self):
        """
        тестирование вывода 1 публикации
        """
        response = self.client.get(
            '/publication/detail/' + str(self.publication.id)
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.OK
        )

    def test_update_publication(self):
        """
        тестирование изменения публикации (изменения вносит только автор и админ)
        """
        data = {
            'name': self.publication.name,
            'description': self.publication.description,
        }
        response = self.client.patch(
            '/publication/update/' + str(self.publication.id),
            data=data
        )
        self.assertEqual(
            response.status_code,
            405
        )

    def test_delete_publication(self):
        """
        Тестирование удаления публикации (удаляет только автор и админ)
        """
        response = self.client.delete(
            '/publication/delete/' + str(self.publication.id)
        )
        self.assertEqual(
            response.status_code,
            404
        )
