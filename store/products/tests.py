from django.test import TestCase
from django.urls import reverse
from django import setup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
setup()


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse("index")
        response = self.client.get(path=path)
        print(response)
        print("Hello from test_view!")
