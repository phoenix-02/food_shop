from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from shop.models import Company


class URLTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='mango', password="1!2@3#4$")
        Company.objects.create(title="some company")

    def test_companies_view_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/companies/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_companies_create_success(self):
        self.client.login(username='mango', password="1!2@3#4$")
        response = self.client.post('/api/companies/', data={'title': "new_comp"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"id": 2, "title": "new_comp"})

    def test_companies_create_not_valid_data_fail(self):
        response = self.client.post('/api/companies/', data={'name': "not valid field value"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_companies_create_access_fail(self):
        response = self.client.post('/api/companies/', data={'title': "new_comp"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
