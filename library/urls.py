"""
URL's for the pages related to the user's folio library
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_library, name="view_library"),
    path('create_folio/', views.create_folio, name="create_folio")
]
