"""
URL's for the pages related to the license store
"""

from django.urls import path
from . import views


urlpatterns = [
    path('purchase/', views.purchase_license, name="purchase_license"),
    path('history/', views.order_history, name="order_history"),
]
