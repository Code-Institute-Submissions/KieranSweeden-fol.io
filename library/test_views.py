""" Testing for views within library app """

from django.test import TestCase
from django.contrib.auth.models import User

from suite.models import Folio
from .views import (
    view_library,
    create_folio,
    update_folio,
    toggle_folio_published_state,
    delete_folio
)

from urllib.parse import urlencode


class TestViews(TestCase):
    """ Testing for user account model within account app """

    def setUp(self):
        self.user = User.objects.create(
            email="test_user@testing.com",
            username="test_user",
            password="password_123",
        )
        self.stored_folio = Folio.objects.create(
            name="this is a stored folio",
            description="this is a stored folio description",
            author_id=self.user
        )
        self.folio_data_only = urlencode({
            'name': "test folio",
            'description': "this is a test folio description.",
            'submit_only': ''
        })
        self.folio_data_and_suite = urlencode({
            'name': "test folio",
            'description': "this is a test folio description.",
            'submit_and_suite': ''
        })
        self.client.force_login(self.user)

    def test_view_library_page(self):
        """ Test the rendering of view library page """
        response = self.client.get('/library/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/view_library.html')

    def test_return_to_library_after_folio_creation(self):
        """ Test that user is re-directed to libary post folio creation """
        response = self.client.post(
            '/library/create_folio/',
            self.folio_data_only,
            content_type="application/x-www-form-urlencoded")
        self.assertRedirects(response, "/library/")

    def test_redirect_to_suite_after_folio_creation(self):
        """ Test that user is re-directed to libary post folio creation """
        response = self.client.post(
            '/library/create_folio/',
            self.folio_data_and_suite,
            content_type="application/x-www-form-urlencoded")
        new_folio = Folio.objects.get(
            name="test folio",
            description="this is a test folio description.",
            author_id=self.user
        )
        self.assertRedirects(
            response,
            f"/suite/projects/{new_folio.id}/"
        )

    def test_return_to_library_after_folio_update(self):
        """ Test that user is re-directed to library after updating folio """
        response = self.client.post(
            f"/library/update_folio/{self.stored_folio.id}/",
            self.folio_data_only,
            content_type="application/x-www-form-urlencoded",
            follow=True
        )
        self.assertRedirects(response, "/library/")

    def test_redirect_to_suite_after_folio_update(self):
        """ Test that user is re-directed to suite after updating folio """
        response = self.client.post(
            f"/library/update_folio/{self.stored_folio.id}/",
            self.folio_data_and_suite,
            content_type="application/x-www-form-urlencoded",
            follow=True
        )
        self.assertRedirects(
            response,
            f"/suite/projects/{self.stored_folio.id}/"
        )
