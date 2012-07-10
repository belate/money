"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="belate", email="belate@example.com", password="belate")

    def test_index(self):

        response = self.client.get("/")
        self.assertRedirects(response,"/accounts/login/?next=/")

        self.client.login(username="belate", password="belate")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response,"bank/index.html")


