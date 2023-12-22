from django.test import TestCase
from contacts.models import Contact


class ContactModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(name='Maria', phone='+79205552211', message='Hello, world!')

    def test_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_phone_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Телефон')

    def test_message_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('message').verbose_name
        self.assertEquals(field_label, 'Сообщение')

    def test_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_phone_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('phone').max_length
        self.assertEquals(max_length, 16)
