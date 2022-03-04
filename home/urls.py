"""
URL for the home page of folio
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home")
]
