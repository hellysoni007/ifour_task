from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class UserAuthTests(APITestCase):
    def test_user_registration(self):
        url = reverse('register')
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'Pass@123'}
        response = self.client.post
