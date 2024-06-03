from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from myApp.models import PerfilAdministrador

class UserRegistrationTestCase(TestCase):

    def test_user_registration(self):
        response = self.client.post(reverse('create_admin_profile'), data={
            'username': 'newadmin',
            'password': 'newadminpassword'
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='newadmin').exists())
        self.assertTrue(PerfilAdministrador.objects.filter(user__username='newadmin').exists())
