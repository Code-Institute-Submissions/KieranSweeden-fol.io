"""
Contact specific urls within the folio suite
"""

from django.urls import path
from suite import views

contact_urlpatterns = [
    path('contact/',
         views.edit_folio_contact,
         name="edit_folio_contact"),
    path('contact/<int:folio_id>/',
         views.edit_folio_contact,
         name="edit_folio_contact"),
    path('contact/update/<int:folio_id>/',
         views.update_folio_contact,
         name="update_folio_contact")
]
