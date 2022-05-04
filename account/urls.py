"""
URL's for the pages related to the license store
"""

from django.urls import path
from . import views

urlpatterns = [
    path('account-details/', views.account_details, name="account_details"),
    path('billing-details/', views.billing_details, name="billing_details"),
]
