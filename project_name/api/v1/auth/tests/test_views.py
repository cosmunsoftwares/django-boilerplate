from model_mommy import mommy

from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class LoginViewValidTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.profile = mommy.make('custom_profile.Profile', user=self.user)
        self.data = {'username': self.user.username, 'password': 'test'}
        self.response = self.client.post(reverse_lazy('api-v1:login'), self.data)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_token(self):
        self.assertTrue(self.response.json().get('token'))

    def test_profile(self):
        self.assertTrue(self.response.json().get('profile'))


class LoginViewInvalidTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.profile = mommy.make('custom_profile.Profile', user=self.user)
        self.response = self.client.post(reverse_lazy('api-v1:login'), {})

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 400)

    def test_errors(self):
        expected_errors = {
            'errors': {
                'username': ['Este campo é obrigatório.'],
                'password': ['Este campo é obrigatório.']
            }
        }

        self.assertDictEqual(self.response.json(), expected_errors)

    def test_errros_invalid_username(self):
        data = {'username': 'invalid-username', 'password': 'test'}
        response = self.client.post(reverse_lazy('api-v1:login'), data)

        expected_errors = {
            'errors': {
                '__all__': ['Usuário ou senha não conferem.']
            }
        }

        self.assertDictEqual(response.json(), expected_errors)

    def test_errros_invalid_password(self):
        data = {'username': self.user.username, 'password': 'invalid-password'}
        response = self.client.post(reverse_lazy('api-v1:login'), data)

        expected_errors = {
            'errors': {
                '__all__': ['Usuário ou senha não conferem.']
            }
        }

        self.assertDictEqual(response.json(), expected_errors)
