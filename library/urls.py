"""
URL's for the pages related to the user's folio library
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_library, name="view_library"),
    path('create_folio/', views.create_folio, name="create_folio"),
    path('update_folio/<int:folio_id>/',
         views.update_folio,
         name="update_folio"),
    path('toggle_published_state/<int:folio_id>/',
         views.toggle_folio_published_state,
         name="toggle_folio_published_state"),
    path('delete_folio/<int:folio_id>/',
         views.delete_folio,
         name="delete_folio"),
]
