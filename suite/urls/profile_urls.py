"""
Profile specific urls within the folio suite
"""

from django.urls import path
from suite import views

profile_urlpatterns = [
    path('profile/',
         views.edit_folio_profile,
         name="edit_folio_profile"),
    path('profile/<int:folio_id>/',
         views.edit_folio_profile,
         name="edit_folio_profile")
]
