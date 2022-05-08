"""
Testing for forms within account app
"""

from django.test import TestCase
from .forms import AccountDetailsForm, BillingDetailsForm


class TestAccountDetailsForm(TestCase):
    """ Testing for account details form within account app """

    def test_account_fields_only_displayed(self):
        """ Test only account detail fields are displayed """
        form = AccountDetailsForm({})
        self.assertEqual(form.Meta.fields, [
            'profile_picture',
            'first_name',
            'last_name',
            'phone_number',
            'github_profile',
            'linkedin_profile',
        ])

    def test_github_field_accept_urls_only(self):
        form = AccountDetailsForm({
            'github_profile': 'test'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('github_profile', form.errors.keys())
        self.assertEqual(
            form.errors['github_profile'][0], 'Enter a valid URL.'
        )

    def test_linkedin_field_accept_urls_only(self):
        form = AccountDetailsForm({
            'linkedin_profile': 'test'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('linkedin_profile', form.errors.keys())
        self.assertEqual(
            form.errors['linkedin_profile'][0], 'Enter a valid URL.'
        )


class TestBillingDetailsForm(TestCase):
    """ Testing for billing details form within account app """

    def test_billing_fields_only_displayed(self):
        """ Test only billing detail fields are displayed """
        form = BillingDetailsForm({})
        self.assertEqual(form.Meta.fields, [
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_postcode',
            'default_county',
            'default_country',
        ])

    def test_labels_are_correct(self):
        form = BillingDetailsForm({})
        self.assertEqual(
            form.fields[
                'default_street_address1'].label, 'Street Address 1')
        self.assertEqual(
            form.fields[
                'default_street_address2'].label, 'Street Address 2')
        self.assertEqual(
            form.fields[
                'default_town_or_city'].label, 'Town / City')
        self.assertEqual(
            form.fields[
                'default_postcode'].label, 'Post Code')
        self.assertEqual(
            form.fields[
                'default_county'].label, 'County')
        self.assertEqual(
            form.fields[
                'default_country'].label, 'Select Country')
