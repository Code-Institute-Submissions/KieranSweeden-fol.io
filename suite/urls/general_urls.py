"""
General urls regarding the suite specifically
"""

from django.urls import path
from . import views

general_urlpatterns = [
    path('open/', views.open_suite, name="open_suite"),
    path('open/<int:folio_id>/', views.open_suite, name="open_suite"),
    path('select/', views.select_folio, name="select_folio")
]
