from django.test import TestCase
from django.urls import resolve, reverse

from siteapps import views


class SiteUrlsTests(TestCase):
    def test_home_url_is_correct(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')

    def test_mt5_url_is_correct(self):
        mt5_url = reverse('MT5 license')
        self.assertEqual(mt5_url, '/mt5/')

    def test_algotrading_url_is_correct(self):
        algotrading_url = reverse('algotrading')
        self.assertEqual(algotrading_url, '/algotrading/')


class SiteViewsTests(TestCase):
    def test_home_view(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)
