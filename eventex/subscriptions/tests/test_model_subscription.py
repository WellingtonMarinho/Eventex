from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Wellington Marinho',
            cpf='44387618833',
            email='umcorte@gmail.com',
            phone='11951948331'
        )
        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        '''Subscription must have an auto created at attr.'''
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Wellington Marinho', str(self.obj))
