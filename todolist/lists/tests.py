from django.test import TestCase


# Create your tests here.
class SmokeTest(TestCase):
    def test_demo_001(self):
        self.assertTrue(1 + 2 == 4)
