import os
from unittest import TestCase
from fileflood import Flood
from fileflood_ignore import Ignore


class Test(TestCase):

    def setUp(self):
        self.app = Flood(os.path.dirname(__file__), source='src')

    def test_ignore_file(self):

        self.app.use(
            Ignore('a.json')
        )
        self.assertIsNone(self.app.get('a.json'))

    def test_ignore_all(self):

        self.app.use(
            Ignore('**/*.json')
        )
        self.assertIsNone(self.app.get('a.json'))
        self.assertIsNone(self.app.get('data/fruits.json'))


