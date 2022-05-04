""" Here is the configuration for the account app """
from django.apps import AppConfig


class AccountConfig(AppConfig):
    """
    Due to a naming clash with an already
    existing django app, the accounts app
    needed to be clarified with the the
    additional config fields you see below
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
