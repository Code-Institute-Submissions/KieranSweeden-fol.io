"""
Skill specific urls within the folio suite
"""

from django.urls import path
from . import views

skill_urlpatterns = [
    path('skills/',
         views.edit_folio_skills,
         name="edit_folio_skills"),
    path('skills/<int:folio_id>/',
         views.edit_folio_skills,
         name="edit_folio_skills")
]
