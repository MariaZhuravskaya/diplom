from django.test import TestCase
from content.models import Publication


class PublicationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Publication.objects.create(name='Big', description='Bob', price=12000, is_publication=True)

    def test_name_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'наименование статьи')

    def test_description_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'описание')

    def test_image_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'изображение')

    def test_paid_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('paid').verbose_name
        self.assertEquals(field_label, 'бесплатная/платная публикация')

    def test_price_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'стоимость подписки')

    def test_date_creation_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('date_creation').verbose_name
        self.assertEquals(field_label, 'дата создания')

    def test_date_change_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('date_change').verbose_name
        self.assertEquals(field_label, 'дата последнего изменения')

    def test_number_views_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('number_views').verbose_name
        self.assertEquals(field_label, 'количество просмотров')

    def test_is_publication_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('is_publication').verbose_name
        self.assertEquals(field_label, 'опубликовано')

    def test_author_label(self):
        publication = Publication.objects.get(id=1)
        field_label = publication._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'автор статьи')

    def test_name_max_length(self):
        publication = Publication.objects.get(id=1)
        max_length = publication._meta.get_field('name').max_length
        self.assertEquals(max_length, 250)

    def test_price_max_digits(self):
        publication = Publication.objects.get(id=1)
        max_digits = publication._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)
