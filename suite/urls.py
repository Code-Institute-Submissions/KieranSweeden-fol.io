"""
URL's for the pages related to the folio suite
"""

from django.urls import path
from . import views

urlpatterns = [
    path('open/<int:folio_id>/', views.open_suite, name="open_suite"),
    path('select/', views.select_folio, name="select_folio"),
    path('projects/<int:folio_id>/',
         views.view_folio_projects,
         name="view_folio_projects"),
    path('skills/', views.view_folio_skills, name="view_folio_skills"),
    path('profile/', views.view_folio_profile, name="view_folio_profile"),
    path('contact/', views.view_folio_contact, name="view_folio_contact"),
]
