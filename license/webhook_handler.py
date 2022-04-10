"""
Contains the webhook handler class
containing the handlers required
to process payments from stripe
"""

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from account.models import UserAccount

import stripe

stripe.api_key = settings.STRIPE_PRIVATE_KEY


class StripeWebHookHandlers:
    """
    Contains methods that handle
    incoming stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles unknown/unexpected incoming
        webhook events
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_checkout_session_completed(self, event):
        """
        Handles successful stripe checkout sessions
        """

        session = event['data']['object']
        no_of_licenses_purchased = stripe.checkout.Session.list_line_items(
            session['id'])['data'][0]['quantity']

        pid = session.payment_intent
        grand_total = session.amount_total

        # Get logged in user
        user = get_object_or_404(
            User,
            pk=session.metadata.user_id
        )

        # Get user's account
        user_account = get_object_or_404(
            UserAccount,
            pk=user.id
        )

        user_account.add_licences_to_user_account(
            no_of_licenses_purchased
        )

        response_message = (
            f"Webhook received: {event['type']} | "
            f"Purchase was successfully made"
        )

        return HttpResponse(
            content=response_message,
            status=200
        )
    
    def handle_payment_intent_failed(self, event):
        """
        Handles a failed stripe checkout session
        """

        response_message = (
            f"Webhook received: {event['type']} | "
            f"Purchase was unsuccessfully made"
        )

        return HttpResponse(
            content=response_message,
            status=200
        )
        
