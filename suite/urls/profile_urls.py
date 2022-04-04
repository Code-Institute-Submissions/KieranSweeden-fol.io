"""
Profile specific urls within the folio suite
"""

from django.urls import path
from suite import views

profile_urlpatterns = [
     path('profile/',
          views.edit_folio_profile,
          name="edit_folio_profile"),
     path('profile/<int:folio_id>/',
          views.edit_folio_profile,
          name="edit_folio_profile"),
     path('profile/create/<int:folio_id>/',
          views.create_folio_profile,
          name="create_folio_profile"),
     path('profile/update/<int:folio_id>/<int:profile_id>',
          views.update_folio_profile,
          name="update_folio_profile"),
     path('profiles/update/profiles_attached/<int:folio_id>/',
          views.update_profiles_attached_to_folio,
          name="update_profiles_attached_to_folio"),
     path('profile/update/current_and_future/<int:folio_id>/',
          views.update_current_and_future_goal,
          name="update_current_and_future_goal"),
     path('profile/delete/<int:folio_id>/<int:profile_id>',
          views.delete_folio_profile,
          name="delete_folio_profile")
]
