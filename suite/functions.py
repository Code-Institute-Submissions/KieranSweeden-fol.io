"""
This file contains helper functions
that are commonly used within the
suite application.
"""
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from suite.models import Folio


def id_has_been_provided(entity_id):
    """
    Simple function returning true or false
    if id has been provided. Created for
    readability purposes.
    """
    return True if entity_id else False


def user_is_author_of_folio(user, folio_id):
    """
    Checks if the current user is the
    author of the folio using it's id.
    """

    # Grab the folio from the database
    folio = get_object_or_404(Folio, pk=folio_id)

    # Return a boolean value
    return True if folio.author_id == user else False


def sortByID(entity):
    return entity['id']
