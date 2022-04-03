"""
Project specific urls within the folio suite
"""

from django.urls import path
from suite import views

project_urlpatterns = [
    path('projects/',
         views.edit_folio_projects,
         name="edit_folio_projects"),
    path('projects/<int:folio_id>/',
         views.edit_folio_projects,
         name="edit_folio_projects"),
    path('projects/create/<int:folio_id>/',
         views.create_folio_project,
         name="create_folio_project"),
    path('projects/update/<int:folio_id>/<int:project_id>',
         views.update_folio_project,
         name="update_folio_project"),
    path('projects/update/projects_attached/<int:folio_id>/',
         views.update_projects_attached_to_folio,
         name="update_projects_attached_to_folio"),
    path('projects/delete/<int:folio_id>/<int:project_id>',
         views.delete_folio_project,
         name="delete_folio_project")
]
