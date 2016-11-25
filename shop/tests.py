from django.test import TestCase
from django.core.urlresolvers import resolve
from shop.views import dashboard
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
# Create your tests here.
class IndexTest(TestCase):
    def test_root_url_resolves_to_login(self):
        found = resolve('/')
        #测试http://127.0.0.1:8000/'是不是dashboard视图
        self.assertEqual(found.func,dashboard)

    def test_home_page_returns_conrrect_html(self):
        request = HttpRequest()
        response = dashboard(request)
        self.assertTrue(response.content.startswith(b'<html>'))#是否HTML开头
        #self.assertIn()