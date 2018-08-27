import json
from model_mommy import mommy
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse_lazy
from django.test import TestCase

from project_name.api.tests.helpers import BaseTestApiCase

User = get_user_model()


class LoginViewValidTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.data = {'username': self.user.username, 'password': 'test'}
        self.response = self.client.post(reverse_lazy('api-v1:login'), data=json.dumps(self.data),
                                         content_type='application/json')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_token(self):
        self.assertTrue(self.response.json()['token'])


class LoginViewInvalidTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.response = self.client.post(reverse_lazy('api-v1:login'), data=json.dumps({}),
                                         content_type='application/json')

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
        response = self.client.post(reverse_lazy('api-v1:login'), data=json.dumps(data),
                                    content_type='application/json')

        expected_errors = {
            'errors': {
                '__all__': ['Usuário ou senha não conferem.']
            }
        }

        self.assertDictEqual(response.json(), expected_errors)

    def test_errros_invalid_password(self):
        data = {'username': self.user.username, 'password': 'invalid-password'}
        response = self.client.post(reverse_lazy('api-v1:login'), data=json.dumps(data),
                                    content_type='application/json')

        expected_errors = {
            'errors': {
                '__all__': ['Usuário ou senha não conferem.']
            }
        }

        self.assertDictEqual(response.json(), expected_errors)
