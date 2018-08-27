import shutil
from model_mommy import mommy

from django.conf import settings
from django.urls import reverse_lazy
from django.test import TestCase
from django.contrib.auth.models import Permission


class BaseTestCase(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        self.create_user()
        self.create_account()
        self.add_permissions()
        self.login()

    def create_user(self):
        self.user = mommy.make('auth.User', username=self.username)
        self.user.set_password(self.password)
        self.user.save()

    def create_account(self):
        self.account = mommy.make('account.Account', user=self.user)

    def add_permissions(self):
        if hasattr(self, 'permissions'):
            for codename in self.permissions:
                permission = Permission.objects.get(codename=codename)
                self.user.user_permissions.add(permission)

    def login(self):
        self.client.post(reverse_lazy('account:login'), {'username': self.user.username, 'password': self.password})

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.BASE_DIR + '/schedules/media', ignore_errors=True)
