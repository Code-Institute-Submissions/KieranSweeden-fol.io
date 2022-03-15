"""
This file registers models created within this application
to the Django admin panel
"""

from django.contrib import admin
from .models import UserAccount

# Register your models here.

admin.site.register(UserAccount)
