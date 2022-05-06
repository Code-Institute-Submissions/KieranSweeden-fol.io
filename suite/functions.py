"""
This file contains helper functions
that are commonly used within the
suite application.
"""
from django.shortcuts import get_object_or_404
from suite.models import (
    Folio,
    Project,
    Skill,
    Profile
)


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
    folio = get_object_or_404(Folio, pk=folio_id)
    return True if folio.author_id == user else False


def user_is_author_of_snippet(user, snippet_type, snippet_id):
    """
    Checks if the current user is
    the author of the snippet provided
    """
    snippet_models = {
        "project": Project,
        "skill": Skill,
        "profile": Profile
    }
    snippet = get_object_or_404(snippet_models[snippet_type], snippet_id)
    return True if snippet.author_id == user else False


def sort_by_id(entity):
    """
    Returns the id of provided entity
    which can be used for sorting purposes
    """
    return int(entity['id'])


def is_tech_skill(skill):
    """
    Returns true if skill is tech skill
    """
    return True if skill.skill_type == "TECH" else False


def is_soft_skill(skill):
    """
    Returns true if skill is soft skill
    """
    return True if skill.skill_type == "SOFT" else False
