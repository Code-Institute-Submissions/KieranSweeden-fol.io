"""
URL for the pages related to the user's folio library
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_library, name="view_library")
]
