import json
from django.conf import settings
from django.urls import reverse
from django.test import SimpleTestCase


class StaticTests(SimpleTestCase):

    def test_root(self):
        url = reverse('root')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        info = json.loads(r.content.decode('utf8'))
        self.assertEqual(info, {'OCFL REPO': {'root': settings.OCFL_STORAGE_ROOT}})
