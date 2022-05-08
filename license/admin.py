"""
This file registers the license purchase model
to the Django admin panel
"""

from django.contrib import admin
from .models import LicensePurchase

admin.site.register(LicensePurchase)
