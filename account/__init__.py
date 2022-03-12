"""
Contains changes to default settings regarding the account app
"""
from django.apps import AppConfig

DEFAULT_APP_CONFIG = 'account.__init__.AccountConfig'


class AccountConfig(AppConfig):
    """
    Changes the label for this app as the account name already
    exists within django. Without this, django will throw an
    ImproperlyConfigured error.
    """
    name = 'account'
    label = 'folio_account'
