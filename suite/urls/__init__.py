"""
File combining all suite patterns for django
"""

from .general_urls import general_urlpatterns
from .project_urls import project_urlpatterns
from .skill_urls import skill_urlpatterns
from .profile_urls import profile_urlpatterns
from .contact_urls import contact_urlpatterns

urlpatterns = (
    general_urlpatterns +
    project_urlpatterns +
    skill_urlpatterns +
    profile_urlpatterns +
    contact_urlpatterns
)
