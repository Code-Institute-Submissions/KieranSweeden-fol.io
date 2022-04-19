"""
URL's for the pages related to the license store
"""

from django.urls import path
from . import views
from . import webhooks


urlpatterns = [
     path('purchase/', views.purchase_license, name="purchase_license"),
     path('history/', views.order_history, name="order_history"),
     path('checkout/',
          views.create_checkout_session,
          name="create_checkout_session"),
     path('checkout/webhook/',
          webhooks.stripe_webhook,
          name="stripe_webhook"),
     path('success/',
          views.checkout_session_success,
          name="checkout_session_success"),
]
