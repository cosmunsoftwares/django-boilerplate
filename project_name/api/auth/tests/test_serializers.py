from model_mommy import mommy
from datetime import timedelta
from rest_framework.serializers import ValidationError

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.test import TestCase

from project_name.api.auth.serializers import LoginSerializer

User = get_user_model()


class LoginSerializerValidTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.serializer = LoginSerializer(data={'username': self.user.username, 'password': 'test'})

    def test_serializer_is_valid(self):
        self.assertTrue(self.serializer.is_valid())

    def test_serializer_get_token(self):
        self.serializer.is_valid()

        self.assertTrue(self.serializer.get_token())


class LoginSerializerInvalidTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.serializer = LoginSerializer(data={})

    def test_serializer_not_is_valid(self):
        self.assertFalse(self.serializer.is_valid())

    def test_validate_password_invalid(self):
        with self.assertRaises(ValidationError):
            self.serializer.validate({'username': self.user.username, 'password': 'invalid-password'})

    def test_validate_username_invalid(self):
        with self.assertRaises(ValidationError):
            self.serializer.validate({'username': 'invalid-username'})
