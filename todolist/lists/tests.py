# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):

    def test_demo_001(self):
        self.assertTrue(1 + 2 == 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertTrue(found.func == home_page)

    def test_homepage_view_content(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.find("<html>"))
        self.assertTrue(response.content.endswith("</html>"))
        expect_html = render_to_string('home.html')
        print type(expect_html)
        self.assertEqual(response.content.decode("utf-8"), expect_html)
