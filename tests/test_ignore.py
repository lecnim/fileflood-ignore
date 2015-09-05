import os
from unittest import TestCase
from rucola import Rucola
from rucola_ignore import Ignore


class Test(TestCase):

    def setUp(self):
        self.app = Rucola(os.path.dirname(__file__))

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

    def test_ignore_multiple(self):

        self.app.use(
            Ignore('a.json', 'data/fruits.json')
        )
        self.assertIsNone(self.app.get('a.json'))
        self.assertIsNone(self.app.get('data/fruits.json'))
