"""
URL's for the pages related to showcase app
"""

from django.urls import path
from . import views


urlpatterns = [
    path(
        '<int:folio_id>/projects/',
        views.view_folio_projects,
        name='view_folio_projects'
        ),
    path(
        '<int:folio_id>/skills/',
        views.view_folio_skills,
        name='view_folio_skills'
        ),
    path(
        '<int:folio_id>/profile/',
        views.view_folio_profile,
        name='view_folio_profile'
        ),
    path(
        '<int:folio_id>/contact/',
        views.view_folio_contact,
        name='view_folio_contact'
        )
]