from django.test import TestCase
from django.urls import reverse_lazy


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse_lazy('core:home'))

    def test_get(self):
        '''GET / must return status code 200'''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        '''Home must use template index.html'''
        self.assertTemplateUsed(self.response, 'core/index.html')
