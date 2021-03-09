from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Lucas Eduardo", cpf='12345678901',
                    email='lucasabreusilva.98@gmail.com', phone='54-99124-6539')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscrition_email_from(self):
        expect = 'lucasabreusilva.98@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscrition_email_to(self):
        expect = ['lucasabreusilva.98@gmail.com', 'lucasabreusilva.98@gmail.com']

        self.assertSequenceEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Lucas Eduardo',
            '12345678901',
            'lucasabreusilva.98@gmail.com',
            '54-99124-6539'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
