""" Testing for views within account app """

from django.test import TestCase

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UserAccount


class TestViews(TestCase):
    """ Test views within account app """

    def setUp(self):
        """ Creates records for testing purposes """

        self.user = User.objects.create(
            email="test_user@testing.com",
            username="test_user",
            password="password_123",
        )

    def test_view_account_details_page(self):
        """ Tests the rendering of account details page """
        self.client.force_login(self.user)
        response = self.client.get('/account/account-details/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/account_details.html')

    def test_post_to_account_details_page(self):
        """ Tests a user can post updated info to account details page"""
        self.client.force_login(self.user)
        response = self.client.post('/account/account-details/', {
            'first_name': 'test',
            'last_name': 'user',
            'phone_number': '07123456789',
            'github_profile': 'https://github.com/test',
            'linkedin_profile': 'https://linkedin.com/test'
        })
        self.assertEqual(response.status_code, 200)
        updated_account = UserAccount.objects.get(user=self.user)
        self.assertEqual(updated_account.first_name, 'test')

    def test_image_upload_to_account_details_page(self):
        """
        Tests that images are uploaded via the account details page
        and are placed within the profile-pictures directory
        """
        self.client.force_login(self.user)
        response = self.client.post('/account/account-details/', {
            'profile_picture': SimpleUploadedFile(
                name='test_image.jpg',
                content=open(
                    'static/images/no-profile-picture.png',
                    'rb').read(),
                content_type='image/png'
            )
        })
        self.assertEqual(response.status_code, 200)
        updated_account = UserAccount.objects.get(user=self.user)
        self.assertEqual(
            updated_account.profile_picture,
            'profile-pictures/test_image.jpg'
        )

    def test_view_billing_details_page(self):
        """ Tests the rendering of billing details page """
        self.client.force_login(self.user)
        response = self.client.get('/account/billing-details/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/billing_details.html')

    def test_post_to_billing_details_page(self):
        """ Tests a user can post updated info to billing details page"""
        self.client.force_login(self.user)
        response = self.client.post('/account/billing-details/', {
            'default_street_address1': '123',
            'default_street_address2': 'test street',
            'default_town_or_city': 'test city',
            'default_county': 'test county',
            'default_postcode': 'TE12 S34',
            'default_country': 'GB'
        })
        self.assertEqual(response.status_code, 200)
        updated_account = UserAccount.objects.get(user=self.user)
        self.assertEqual(updated_account.default_county, 'test county')
