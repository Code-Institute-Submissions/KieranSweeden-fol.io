"""
Skill specific urls within the folio suite
"""

from django.urls import path
from suite import views

skill_urlpatterns = [
     path('skills/',
          views.edit_folio_skills,
          name="edit_folio_skills"),
     path('skills/<int:folio_id>/',
          views.edit_folio_skills,
          name="edit_folio_skills"),
     path('skills/create/<int:folio_id>/',
          views.create_folio_skill,
          name="create_folio_skill"),
     path('skills/update/<int:folio_id>/<int:skill_id>',
          views.update_folio_skill,
          name="update_folio_skill"),
     path('skills/update/skills_attached/<int:folio_id>/',
          views.update_skills_attached_to_folio,
          name="update_skills_attached_to_folio"),
     path('skills/delete/<int:folio_id>/<int:skill_id>',
          views.delete_folio_skill,
          name="delete_folio_skill")
]
