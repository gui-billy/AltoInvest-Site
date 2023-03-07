from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone

from apps import views
from apps.models import Clients


class SiteUrlsTests(TestCase):
    def test_home_url_is_correct(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')

    def test_mt5_url_is_correct(self):
        mt5_url = reverse('MT5 license')
        self.assertEqual(mt5_url, '/mt5/')


class SiteViewsTests(TestCase):
    def test_home_view(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    def test_mt5_view(self):
        view = resolve(reverse('MT5 license'))
        self.assertIs(view.func, views.mt5_view)

    def test_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def setUp(self):
        self.test_client = Clients.objects.create(
            name='John Doe',
            broker='Brokerage Inc.',
            account=123456,
            exp_date=timezone.now().date()
        )

    def test_client_str(self):
        client = self.test_client
        self.assertEqual(client.__str__(), 'John Doe')
