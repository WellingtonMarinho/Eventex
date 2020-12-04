from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Wellington Marinho', cpf='12345678901',
                    email='umcorte@gmail.com', phone='11-951948331')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'umcorte@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['umcorte@gmail.com', 'umcorte@gmail.com']
        self.assertEqual(expect, self.email.to)

    # def test_subscription_email_body(self):
    #     email = mail.outbox[0]
    #     self.assertIn('Wellington Marinho', self.email.body)

    def test_subscription_email_body(self):
        contents = ['Wellington Marinho', '12345678901', 'umcorte@gmail.com', '11-951948331']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
