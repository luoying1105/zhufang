from django.test import TestCase
from django.core.urlresolvers import resolve
from shop.views import dashboard
from django.contrib.auth import authenticate, login
# Create your tests here.
class IndexTest(TestCase):
    def test_root_url_resolves_to_login(self):
        found = resolve('/')
        #测试http://127.0.0.1:8000/'是不是dashboard视图
        self.assertEqual(found.func,dashboard)
