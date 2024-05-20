import json

from django.test import TestCase
from django.urls import reverse

from myApp.models import PerfilAdministrador

class PerfilAdministrador(TestCase):

    @classmethod
    def setUpTestData(cls):
        PerfilAdministrador.objects.create(
            user = 'admin',
            password = 'admin'
        )

    def test_create_admin(self):
        response = self.client.post('/myApp/createAdminProfile', data={
            'user': 'admin',
            'password': 'admin'
        })

        self.assertIn(response.status_code, [200, 201])
        filtered_user = PerfilAdministrador.objects.filter(user='admin').first()
        self.assertEqual(filtered_user.password, 'admin')
