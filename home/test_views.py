"""
Test home app views
"""

from django.test import TestCase


class TestViews(TestCase):
    """
    Test home app views
    """

    def test_home_view(self):
        """Tests the home app view rendered correctly"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
