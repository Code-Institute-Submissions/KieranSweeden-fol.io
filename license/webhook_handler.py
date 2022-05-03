"""
Contains the webhook handler class
containing the handlers required
to process payments from stripe
"""

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from account.models import UserAccount
from .models import LicensePurchase

import stripe

stripe.api_key = settings.STRIPE_PRIVATE_KEY


class StripeWebHookHandlers:
    """
    Contains methods that handle
    incoming stripe webhooks
    """

    def handle_event(self, event):
        """
        Handles unknown/unexpected incoming
        webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_checkout_session_completed(self, event):
        """Handles successful stripe checkout sessions"""

        session = event['data']['object']
        no_of_licenses_purchased = (
            stripe.checkout.Session.list_line_items(
                session['id'])['data'][0]['quantity']
            )
        customer_details = session['metadata']

        user = get_object_or_404(
            User,
            pk=customer_details.user_id
        )

        new_license_purchase = LicensePurchase(
            user=user,
            purchaser_full_name=customer_details['purchaser_full_name'],
            purchaser_email=session['customer_email'],
            purchaser_phone_number=customer_details['purchaser_phone_number'],
            purchaser_street_address1=customer_details[
                'purchaser_street_address1'],
            purchaser_street_address2=customer_details[
                'purchaser_street_address2'],
            purchaser_town_or_city=customer_details['purchaser_town_or_city'],
            purchaser_postcode=customer_details['purchaser_postcode'],
            purchaser_county=customer_details['purchaser_county'],
            purchaser_country=customer_details['purchaser_country'],
            no_of_licenses_purchased=no_of_licenses_purchased,
            purchase_total=session.amount_total,
            stripe_pid=session.payment_intent
        )

        new_license_purchase.purchase_total /= 100
        new_license_purchase.save()

        email_subject = render_to_string(
            'license/includes/email/purchase_confirmation_subject.txt',
            {"order_number": new_license_purchase.order_number}
        )

        email_body = render_to_string(
            'license/includes/email/purchase_confirmation_body.txt',
            {
                "purchase": new_license_purchase,
                "contact_email": settings.DEFAULT_FROM_EMAIL
            }
        )

        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [session['customer_email']]
        )

        user_account = get_object_or_404(
            UserAccount,
            pk=user.id
        )

        user_account.add_licences_to_user_account(
            no_of_licenses_purchased
        )

        if 'save_billing_as_default' in customer_details:
            user_account.save_purchase_info_as_default(
                customer_details=customer_details
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
