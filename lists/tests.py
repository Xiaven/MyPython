from django.test import TestCase
from django.core.urlresolvers import resolve

from lists.views import home_page
from django.http import HttpRequest
# Create your tests here.
class HomePageTest(TestCase):

    def test_RootURL_resolveTo_HomePage_View(self):
        found=resolve('/')
        self.assertEquals(found.func,home_page)

    def test_HomePage_return_correctHtml(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))