import json
import base64

from django.conf import settings
from django.urls import reverse_lazy

from project_name.core.tests.helpers import BaseTestCase


class BaseTestApiCase(BaseTestCase):

    def setUp(self):
        super(BaseTestApiCase, self).setUp()
        self.headers = self._get_headers()

    def _get_headers(self):
        data = {"username": self.username, "password": self.password}
        response = self.client.post(reverse_lazy('api-v1:login'), data=json.dumps(data),
                                    content_type='application/json')

        token = response.json()['token']

        return {
            'Content-Type': 'application/json',
            'HTTP_AUTHORIZATION': f'Basic {token}',
            'Accept-Language': 'pt-br',
        }
