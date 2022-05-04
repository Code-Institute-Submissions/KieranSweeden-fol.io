""" Testing for forms within account app """

from django.test import TestCase

from django.contrib.auth.models import User
from .forms import AccountDetailsForm


class TestForms(TestCase):
    """ Testing for forms within account app """

    def setUp(self):
        """ Creates records for testing purposes """

        self.user = User.objects.create(
            email="test_user@testing.com",
            username="test_user",
            password="password_123",
        )