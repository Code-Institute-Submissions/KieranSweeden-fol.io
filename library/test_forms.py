"""
Testing for forms within account app
"""

from django.test import TestCase

from .forms import CreateFolioForm


class TestCreateFolioForm(TestCase):
    """ Testing for create folio form within library app """

    def test_create_folio_fields_only_displayed(self):
        """ Test that only create folio fields are displayed """
        form = CreateFolioForm({})
        self.assertEqual(form.Meta.fields, [
            'name',
            'description'
        ])
