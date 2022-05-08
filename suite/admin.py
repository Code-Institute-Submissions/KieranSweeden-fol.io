"""
Registers the folio, project,
skill and profile models to django's admin console
"""
from django.contrib import admin
from .models import Folio, Project, Skill, Profile

admin.site.register(Folio)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Profile)
