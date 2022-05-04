""" Testing for user account model within account app """

from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserAccount


class TestUserAccountModel(TestCase):
    """ Testing for user account model within account app """

    def setUp(self):
        """ Creates records for testing purposes """

        self.user = User.objects.create(
            email="test_user@testing.com",
            username="test_user",
            password="password_123",
        )

    def test_increment_number_of_licenses(self):
        """ Ensure the number of licenses increments correctly """
        self.client.force_login(self.user)
        user_account = UserAccount.objects.get(user=self.user)
        self.assertEqual(user_account.number_of_licenses, 0)
        user_account.add_licences_to_user_account(1)
        self.assertEqual(user_account.number_of_licenses, 1)
        user_account.add_licences_to_user_account(2)
        self.assertEqual(user_account.number_of_licenses, 3)

    def test_default_billing_info_is_saved(self):
        """ Ensure billing info from license purchase is saved """
        self.client.force_login(self.user)
        user_account = UserAccount.objects.get(user=self.user)
        user_account.save_purchase_info_as_default({
            'purchaser_street_address1': 'testing',
            'purchaser_street_address2': 'street',
            'purchaser_town_or_city': 'test town',
            'purchaser_postcode': 'testing',
            'purchaser_county': 'test',
            'purchaser_country': 'GB'
        })
        self.assertEqual(
            user_account.default_street_address1,
            'testing'
        )

    def test_full_name_is_returned(self):
        """ Tests that a full name is returned """
        self.client.force_login(self.user)
        user_account = UserAccount.objects.get(user=self.user)
        user_account.first_name = "testing"
        user_account.last_name = "user"
        full_name = user_account.get_full_name()
        self.assertEqual(full_name, "testing user")

    def test_email_is_returned(self):
        """ Test email is returned as string """
        self.client.force_login(self.user)
        user_account = UserAccount.objects.get(user=self.user)
        self.assertEqual(user_account.__str__(), "test_user@testing.com")
