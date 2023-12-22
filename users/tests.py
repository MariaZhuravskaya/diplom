from django.test import TestCase
from django.test import Client
from http import HTTPStatus


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_is_ok_page_login(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_register(self):
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)
